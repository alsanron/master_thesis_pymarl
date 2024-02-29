import numpy as np
import os
import collections
from os.path import dirname, abspath
from copy import deepcopy
from sacred import Experiment, SETTINGS
from sacred.observers import FileStorageObserver
from sacred.utils import apply_backspaces_and_linefeeds
import sys
import torch as th
from utils.logging import get_logger
import yaml

from run import run

SETTINGS['CAPTURE_MODE'] = "fd" # set to "no" if you want to see stdout/stderr in console
logger = get_logger()

ex = Experiment("pymarl")
ex.logger = logger
ex.captured_out_filter = apply_backspaces_and_linefeeds # makes filtering easier

results_path = os.path.join(dirname(dirname(abspath(__file__))), "results")

@ex.main
def my_main(_run, _config, _log):
    # Setting the random seed throughout the modules
    config = config_copy(_config)
    np.random.seed(config["seed"])
    th.manual_seed(config["seed"])
    config['env_args']['seed'] = config["seed"]

    # run the framework
    run(_run, config, _log)


def _get_config(params, arg_name, subfolder):
    config_name = None
    for _i, _v in enumerate(params):
        if _v.split("=")[0] == arg_name:
            config_name = _v.split("=")[1] 
            del params[_i]
            break

    if config_name is not None:
        with open(os.path.join(os.path.dirname(__file__), "config", subfolder, "{}.yaml".format(config_name)), "r") as f:
            try:
                config_dict = yaml.load(f, Loader=yaml.SafeLoader)
            except yaml.YAMLError as exc:
                assert False, "{}.yaml error: {}".format(config_name, exc)
        return config_dict
    
def _get_param(params, arg_name, type):
    config_name = None
    for _i, _v in enumerate(params):
        if _v.split("=")[0] == arg_name:
            config_name = type(_v.split("=")[1])  # Cast config_name to type
            del params[_i]
            return config_name

    raise ValueError("Argument {} not found in params".format(arg_name))


def recursive_dict_update(d, u):
    for k, v in u.items():
        if isinstance(v, collections.ChainMap):
            d[k] = recursive_dict_update(d.get(k, {}), v)
        else:
            d[k] = v
    return d


def config_copy(config):
    if isinstance(config, dict):
        return {k: config_copy(v) for k, v in config.items()}
    elif isinstance(config, list):
        return [config_copy(v) for v in config]
    else:
        return deepcopy(config)


if __name__ == '__main__':
    params = deepcopy(sys.argv)

    # Get the defaults from default.yaml    
    with open(os.path.join(os.path.dirname(__file__), "config", "default.yaml"), "r") as f:
        try:
            config_dict = yaml.load(f, Loader=yaml.SafeLoader)
        except yaml.YAMLError as exc:
            assert False, "default.yaml error: {}".format(exc)

    # Load algorithm and env base configs for the specified algorithm and env ->
    # they overwrite default values
    batch_job = _get_param(params, "--batch_job", bool)

    settings_path = "research/job_scheduler/batches_ongoing" if batch_job else "research"

    research_config = _get_config(params, "--research_config", settings_path)
    
    # wrapper to make it work with the new config
    wrapper_list = ["--env-config={}".format(research_config["env"]),
                    "--config={}".format(research_config["algorithm"])]
    
    env_config = _get_config(wrapper_list, "--env-config", "envs")
    alg_config = _get_config(wrapper_list, "--config", "algs")

    # Updates default configuration params with new values
    config_dict = recursive_dict_update(config_dict, env_config)
    config_dict = recursive_dict_update(config_dict, alg_config)
    
    # research config has higher priority
    config_dict = recursive_dict_update(config_dict, research_config)

    exp_label = config_dict["label"]
    results_path = os.path.join(results_path, exp_label)
    os.makedirs(results_path, exist_ok=True)

    ex.add_config(config_dict)

    # Save to disk by default for sacred
    logger.info("Saving to FileStorageObserver in results/sacred.")
    file_obs_path = os.path.join(results_path, "sacred")
    ex.observers.append(FileStorageObserver.create(file_obs_path))
    
    ex.run_commandline(params)