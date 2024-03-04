import matplotlib.pyplot as plt
import numpy as np
from plt_tools import include_plot, load_data

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


# generate_training_figure(["qmix_3m_baseline", "qmix_3m_to_3m_direct", "qmix_3m_to_3m_grad_unfreeze_05"], label="qmix_3m_self_transfer.png")
    
# generate_training_figure(["qmix_3m_baseline", "qmix_8m_to_3m_direct", "qmix_8m_to_3m_grad_unfreeze_02", 
#                           "qmix_8m_to_3m_grad_unfreeze_05", "qmix_8m_to_3m_grad_unfreeze_inf"], label="qmix_8m_to_3m_transfer.png")
    
generate_training_figure(["qmix_8m_baseline", "qmix_3m_to_8m_direct"], label="qmix_3m_8m_transfer.png")

# generate_training_figure(["qmix_8m_baseline"], label="8m_qmix_baseline.png")

# generate_basic_figure(["qmix_3m_baseline"], label="3m_qmix_baseline.png")

# generate_plot('battle_won_mean', ['baselines/3m_qmix', 'qmix_8m_to_3m'], with_std=False, show=True)
# generate_plot('return', ['baselines/3m_qmix', 'qmix_8m_to_3m'], with_std=True, show=True)

# generate_plot('test_battle_won_mean', ['baselines/3m_qmix', 'qmix_8m_to_3m'], with_std=False, show=True)
# generate_plot('test_return', ['baselines/3m_qmix', 'qmix_8m_to_3m'], with_std=True, show=True)


