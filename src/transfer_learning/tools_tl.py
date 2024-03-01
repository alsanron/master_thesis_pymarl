import torch as th
import os
from os.path import dirname, abspath
import json

data_path = os.path.join(dirname(dirname(dirname(abspath(__file__)))), "research", "data")
baselines_path = os.path.join(data_path, "baselines")

def get_list_of_baseline_models():
    # Get the list of baseline models
    baseline_models = os.listdir(baselines_path)

    return baseline_models

def extract_gru_params(state_dict):
    # Extract the GRU parameters from the state_dict
    gru_params = {}
    for name, param in state_dict.items():
        if "rnn" in name:
            name = name.split("rnn.")[1]
            gru_params[name] = param

    return gru_params


def load_model(model:str, timestep:int=0, agent="rnn"):
    # Define the path to the baseline model based on the model 
    baseline_path = f"{baselines_path}/{model}"
    model_path = f"{baseline_path}/models"
    results_path = f"{baseline_path}/sacred/info.json"

    if not os.path.isdir(baseline_path): raise ValueError(f"Model {model} not found on {baseline_path}")

    # Go through all files in args.checkpoint_path
    timesteps = []
    for name in os.listdir(model_path):
        full_name = os.path.join(model_path, name)
        # Check if they are dirs the names of which are numbers
        if os.path.isdir(full_name) and name.isdigit():
            timesteps.append(int(name))

    if timestep == 0:
        # choose the max timestep
        timestep_to_load = max(timesteps)
    else:
        # choose the timestep closest to load_step
        timestep_to_load = min(timesteps, key=lambda x: abs(x - timestep))

    model_path = os.path.join(model_path, str(timestep_to_load))
    results = json.load(open(results_path, "r"))

    th_data = th.load("{}/agent.th".format(model_path), map_location=lambda storage, loc: storage)

    return th_data, results


# Some tests

# model, results = load_model("3m_qmix", 0, "rnn")

