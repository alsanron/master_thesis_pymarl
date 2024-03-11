import matplotlib.pyplot as plt
import numpy as np
from plt_tools import include_plot, load_data

def generate_training_figure(models:list, label:str, only_last_legend:bool=False):
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

        if only_last_legend:
            if i == len(variables) - 1:
                ax.legend()
        else:
            ax.legend()
    
    plt.tight_layout()
    if label:
        plt.savefig("figures/" + label)
    plt.show()

