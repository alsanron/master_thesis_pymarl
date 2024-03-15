import pandas as pd
import numpy as np
from plt_tools import load_data
from tl_metrics import auc_ratio

# List of file paths to read
file_paths = ['/path/to/file1.csv', '/path/to/file2.csv', '/path/to/file3.csv']

# Create an empty DataFrame to store the data
data = pd.DataFrame()

# Read each file and append the data to the DataFrame
for file_path in file_paths:
    df = pd.read_csv(file_path)
    data = data.append(df)

# Save the data to an ods format file
output_file_path = '/path/to/output.ods'
data.to_excel(output_file_path, engine='odf')

def generate_training_figure(models:list, label:str, only_last_legend:bool=False, baseline:str=None, median:bool=False):
    fig, axes = plt.subplots(2, 2, figsize=(20, 8))
    variables = ['battle_won_mean', 'test_battle_won_mean', 'return_mean', 'test_return_mean', 
                #  'ep_length_mean', 'epsilon', 'loss', 'wall_time_min'
                 ]

    data_list = []; ratios_auc = []
    for model in models:
        data_list.append(load_data(model, median=median))

        if baseline:
            ratios_auc.append(auc_ratio(baseline, [model], "battle_won_mean", "trapezoid", median=median)[0])

    
    for i, variable in enumerate(variables):
        ax = axes[i // 2, i % 2]

        for ii in range(len(models)):
            if variable in data_list[ii]:
                label_plot = models[ii] + f" ({ratios_auc[ii]:.2f})" if baseline else models[ii]

                if median:
                    include_plot_median(ax, data_list[ii][variable + '_T'], 
                                 data_list[ii][variable + "_median"], 
                                 data_list[ii][variable + "_p25"],
                                  data_list[ii][variable + "_p75"], label=label_plot)
                else:
                    include_plot_mean(ax, data_list[ii][variable + '_T'], 
                                 data_list[ii][variable + "_avg"], 
                                 data_list[ii][variable + "_std"], label=label_plot)
                
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