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

# generate_training_figure(["3m_rnn_qmix", "3m_rnn-pad56_qmix", "3m_rnn-pad128_qmix", "3m_rnn-pad512_qmix"], label="3m_rnn-pad_qmix.png")

# generate_training_figure(["3m_rnn_qmix", "3m_from-3m_rnn_qmix_direct", "3m_from-3m_rnn_qmix_unfreeze02",
#                           "3m_from-3m_rnn_qmix_unfreeze05", "3m_from-3m_rnn_qmix_unfreezeinf"], label="3m_selftransfer_rnn_qmix.png")

# generate_training_figure(["3m_rnn_qmix", "3m_from-8m_rnn_qmix_direct", "3m_from-8m_rnn_qmix_unfreeze0.2",
#                           "3m_from-8m_rnn_qmix_unfreeze0.5", "3m_from-8m_rnn_qmix_unfreezeinf", "3m_from-8m_rnn-pad512_qmix_unfreeze0.2"], label="3m_from-8m_rnn_qmix.png")

# generate_training_figure(["8m_rnn_qmix", "8m_rnn-pad512_qmix"], label="8m_rnn-pad_qmix.png")

# generate_training_figure(["8m_rnn_qmix", "8m_from-8m_rnn_qmix_direct", "8m_from-8m_rnn_qmix_unfreeze02",
#                           "8m_from-8m_rnn_qmix_unfreeze05", "8m_from-8m_rnn_qmix_unfreezeinf"], label="8m_selftransfer_rnn_qmix.png")

# generate_training_figure(["8m_rnn_qmix", "8m_from-3m_rnn_qmix_direct", "8m_from-3m_rnn_qmix_unfreeze0.2",
#                           "8m_from-3m_rnn_qmix_unfreeze0.5", "8m_from-3m_rnn_qmix_unfreezeinf", "wrong_8m_from-3m_rnn-pad512_qmix_unfreeze0.2",
#                           "8m_from-3m_rnn-pad512_qmix_unfreeze0.2"
#                           ], label="8m_from-3m_rnn_qmix.png")

# generate_training_figure(["25m_rnn_qmix"], label="25m_rnn_qmix.png")

# generate_training_figure(["25m_from-8m_rnn_qmix_unfreeze0.2"], label="trash_25m_rnn_qmix.png")

# generate_training_figure(["2m_vs_1z_rnn_qmix"], label="2m_vs_1z_rnn_qmix.png")

# generate_training_figure(["2s3z_rnn_qmix"], label="2s3z_rnn_qmix.png")

# generate_training_figure(["3s_vs_3z_rnn_qmix"], label="3s_vs_3z_rnn_qmix.png")

# generate_training_figure(["3s_vs_4z_rnn_qmix"], label="3s_vs_4z_rnn_qmix.png")

# generate_training_figure(["3s5z_rnn_qmix"], label="3s5z_rnn_qmix.png")

generate_training_figure(["5m_vs_6m_rnn_qmix"], label="5m_vs_6m_rnn_qmix.png")

# generate_training_figure(["6h_vs_8z_rnn_qmix"], label="6h_vs_8z_rnn_qmix.png")

# generate_training_figure(["2m_vs_1z_rnn_qmix"], label="2m_vs_1z_rnn_qmix.png")
