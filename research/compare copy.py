import json
import os
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


def listOfDict_to_listOfValues(input:list) -> list:
    return [d["value"] for d in input]

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

def generate_training_figure(models:list, label:str):
    fig, axes = plt.subplots(4, 2, figsize=(20, 8))
    variables = ['battle_won_mean', 'test_battle_won_mean', 'return_mean', 'test_return_mean', 'ep_length_mean', 'epsilon', 'loss', 'wall_time_min']
    
    for i, variable in enumerate(variables):
        ax = axes[i // 2, i % 2]
        for model in models:
            data = load_data(model)

            if variable in data:
                include_plot(ax, data[variable + '_T'], data[variable + "_avg"], data[variable + "_std"], label=model)
        ax.grid()
        ax.set_xlabel('Timesteps')
        ax.set_ylabel(variable)
        ax.legend()
    
    plt.tight_layout()
    if label:
        plt.savefig("figures/" + label)
    plt.show()



generate_training_figure(["qmix_3m_baseline"], label="qmix_3m_baseline.png")

# generate_basic_figure(["qmix_3m_baseline"], label="3m_qmix_baseline.png")

# generate_basic_figure(["qmix_3m_baseline"], label="3m_qmix_baseline.png")

# generate_plot('battle_won_mean', ['baselines/3m_qmix', 'qmix_8m_to_3m'], with_std=False, show=True)
# generate_plot('return', ['baselines/3m_qmix', 'qmix_8m_to_3m'], with_std=True, show=True)

# generate_plot('test_battle_won_mean', ['baselines/3m_qmix', 'qmix_8m_to_3m'], with_std=False, show=True)
# generate_plot('test_return', ['baselines/3m_qmix', 'qmix_8m_to_3m'], with_std=True, show=True)


