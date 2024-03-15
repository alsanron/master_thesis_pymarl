import torch as th
import os


# Define the path to the baseline model based on the model 
model_path = f"freezing_weights"

# Go through all files in args.checkpoint_path
timesteps = []
for name in os.listdir(model_path):
    full_name = os.path.join(model_path, name)
    # Check if they are dirs the names of which are numbers
    if os.path.isdir(full_name) and name.isdigit():
        timesteps.append(int(name))

def calculate_delta_parameters(model_t0:dict, model_t1:dict):
    delta_parameters = {}
    for key in model_t0.keys():
        if isinstance(model_t0[key], th.Tensor):
            delta_parameters[key] = model_t1[key] - model_t0[key]
    return delta_parameters


delta_weights = []
timesteps.sort()
for i in range(len(timesteps) - 1):
    current_path = os.path.join(model_path, str(timesteps[i]), "agent.th")
    next_path = os.path.join(model_path, str(timesteps[i+1]), "agent.th")

    current_weights = th.load(current_path, map_location=lambda storage, loc: storage)
    next_weights = th.load(next_path, map_location=lambda storage, loc: storage)

    delta = calculate_delta_parameters(current_weights, next_weights)
    delta_weights.append(delta)

a=2