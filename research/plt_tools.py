import json
import os
import matplotlib.pyplot as plt
import numpy as np


def include_plot(axes, x, y_avg, y_std=[], label=""):
    axes.plot(x, y_avg, label=label)

    if len(y_std):
        axes.fill_between(x, y_avg - np.array(y_std), y_avg + np.array(y_std), alpha=0.3)

        
def are_same_timesteps(ts1, ts2, tolerance:int=100) -> bool:
    if len(ts1) != len(ts2):
        return False
    
    diff = 0
    for i in range(len(ts1)):
        diff += abs(ts1[i] - ts2[i])
    diff /= len(ts1)

    return diff < tolerance


def to_numeric_list(input: list) -> list:
    if all(isinstance(x, dict) for x in input):
        return [x["value"] for x in input]
    else:
        return input
    

def load_data(model:str):
    variables = ['battle_won_mean', 'test_battle_won_mean', 'return_mean', 'test_return_mean',
                 'ep_length_mean', 'epsilon', 'loss', 'q_taken_mean', 'wall_time_min']
    data = {}

    for file in os.listdir("data/" + model + "/sacred"):
        if file.isnumeric():
            data_temp = json.load(open("data/" + model + "/sacred/" + file + "/info.json"))
            for variable in variables:
                if variable in data_temp:
                    if not variable in data:
                        data[variable + "_T"] = data_temp[variable + "_T"]
                        
                        data[variable] = [to_numeric_list(data_temp[variable])]
                    else:
                        # if not are_same_timesteps(data[variable + "_T"], data_temp[variable + "_T"]):
                        #     raise ValueError("Timesteps are not the same for all experiments")
                        
                        data[variable].append(to_numeric_list(data_temp[variable]))

    for variable in variables:
        if variable in data:
            data[variable + "_avg"] = np.average(data[variable], axis=0)
            data[variable + "_std"] = np.std(data[variable], axis=0)

    return data