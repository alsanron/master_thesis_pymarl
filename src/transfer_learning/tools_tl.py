import torch as th
import os
from os.path import dirname, abspath
import json
import random

data_path = os.path.join(dirname(dirname(dirname(abspath(__file__)))), "research", "data")

def extract_layer_params(state_dict, layer_name):
    # Extract the GRU parameters from the state_dict
    layer_params = {}
    for name, param in state_dict.items():
        if layer_name in name:
            name = name.split("{}.".format(layer_name))[1]
            layer_params[name] = param

    return layer_params



def sample_subfolder_randomly(model_path):
    subfolders = [f for f in os.listdir(model_path) if os.path.isdir(os.path.join(model_path, f))]
    return random.choice(subfolders)


def load_model(model:str, timestep:int=0, agent="rnn"):
    # Define the path to the baseline model based on the model 
    model_path = f"{data_path}/{model}/models"

    # Samplees randomly one of the trained models
    model_path = os.path.join(model_path, sample_subfolder_randomly(model_path))

    if not os.path.isdir(model_path): raise ValueError(f"Model {model} not found on {model_path}")

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

    th_data = th.load("{}/agent.th".format(model_path), map_location=lambda storage, loc: storage)

    return th_data
