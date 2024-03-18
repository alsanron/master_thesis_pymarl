from main_plot import generate_training_figure


############ BLOCK 1 ############
generate_training_figure(["baselines/3m_rnn_coma", 
                          # "3m_from-3m_rnn_coma_unfreeze0.2", 
                          # "3m_from-8m_rnn_coma_unfreeze0.2",
                          # "3m_from-25m_rnn_coma_unfreeze0.2", 
                        #   "3m_from-5m_rnn_coma_unfreeze0.2" # currently it doesnt train properly
                          ], 
                          label="tl_coma/3m_rnn_coma.png", 
                          only_last_legend=True, 
                          baseline="baselines/3m_rnn_coma", median=True)

# generate_training_figure(["3m_rnn_coma", "3m_from-2s3z_rnn_coma_unfreeze0.2", "3m_from-3s_rnn_coma_unfreeze0.2",
#                           "3m_from-2m_rnn_coma_unfreeze0.2"], label="tl_coma/3m_rnn_coma_ext.png", 
#                           only_last_legend=True, baseline="3m_rnn_coma", median=True)

generate_training_figure(["baselines/8m_rnn_coma", 
                          # "8m_from-3m_rnn_coma_unfreeze0.2", 
                          # "8m_from-8m_rnn_coma_unfreeze0.2",
                          # "8m_from-25m_rnn_coma_unfreeze0.2", 
                          # "8m_from-3m-8m_rnn_coma_unfreeze0.2_additive", 
                          # "8m_from-3m-8m_rnn_coma_unfreeze0.2_mean"
                        #   "8m_from-5m_rnn_coma_direct"
                          ], 
                          label="tl_coma/8m_rnn_coma.png", only_last_legend=True, 
                          baseline="baselines/8m_rnn_coma", median=True)


generate_training_figure(["baselines/25m_rnn_coma", 
                          # "25m_from-3m_rnn_coma_unfreeze0.2", 
                          # "25m_from-8m_rnn_coma_unfreeze0.2",
                          # "25m_from-25m_rnn_coma_direct", 
                          # "25m_from-25m_rnn_coma_unfreeze0.2",
                        #   "25m_from-5m_rnn_coma_direct"
                          ], label="tl_coma/25m_rnn_coma.png", only_last_legend=True, 
                          baseline="baselines/25m_rnn_coma", median=True)


generate_training_figure(["baselines/5m_vs_6m_rnn_coma", 
                          # "5m_vs_6m_from-3m_rnn_coma_unfreeze0.2", 
                          # "5m_vs_6m_from-8m_rnn_coma_unfreeze0.2",
                          # "5m_vs_6m_from-25m_rnn_coma_unfreeze0.2", "5m_vs_6m_from-5m_rnn_coma_unfreeze0.2",
                          #  "5m_vs_6m_from-3m-8m_rnn_coma_unfreeze0.2_additive",
                          #   "5m_vs_6m_from-3m-8m_rnn_coma_unfreeze0.2_mean",
                          ], label="tl_coma/5m_vs_6m_rnn_coma.png", 
                          only_last_legend=True, 
                          baseline="baselines/5m_vs_6m_rnn_coma", median=True)


############ BLOCK 2 ############
generate_training_figure(["baselines/2s3z_rnn_coma", 
                          # "2s3z_from-3m_rnn_coma_unfreeze0.2", 
                          # "2s3z_from-3s5z_rnn_coma_unfreeze0.2",
                          ], label="tl_coma/2s3z_rnn_coma.png", only_last_legend=True, 
                          baseline="baselines/2s3z_rnn_coma", median=True)


generate_training_figure(["baselines/3s5z_rnn_coma", 
                          # "3s5z_from-2s3z_rnn_coma_unfreeze0.2",
                          ], label="tl_coma/3s5z_rnn_coma.png", 
                          only_last_legend=True, baseline="baselines/3s5z_rnn_coma", median=True)

# ############ BLOCK 3 ############

generate_training_figure(["baselines/3s_vs_3z_rnn_coma", 
                          # "3s_vs_3z_from-3m_rnn_coma_unfreeze0.2", 
                          # "3s_vs_3z_from-3s_rnn_coma_unfreeze0.2",
                          ], label="tl_coma/3s_vs_3z_rnn_coma.png", 
                          only_last_legend=True, baseline="baselines/3s_vs_3z_rnn_coma", median=True)

generate_training_figure(["baselines/3s_vs_4z_rnn_coma", 
                        #   "3s_vs_4z_from-3s_rnn_coma_direct", 
                          # "3s_vs_4z_from-3s_rnn_coma_unfreeze0.2",
                          ], label="tl_coma/3s_vs_4z_rnn_coma.png", 
                          only_last_legend=True, baseline="baselines/3s_vs_4z_rnn_coma", median=True)


# ############ BLOCK 4 ############
generate_training_figure(["baselines/2m_vs_1z_rnn_coma", 
                          # "2m_vs_1z_from-3m_rnn_coma_unfreeze0.2",
                          ], label="tl_coma/2m_vs_1z_rnn_coma.png", 
                          only_last_legend=True, baseline="baselines/2m_vs_1z_rnn_coma", median=True)

# ############ BLOCK 5 ############
generate_training_figure(["baselines/6h_vs_8z_rnn_coma",
                          # "6h_vs_8z_from-2m_rnn_coma_direct", 
                          # "6h_vs_8z_from-3s_rnn_coma_direct",
                          # "6h_vs_8z_from-3m-3s-2m_rnn_coma_direct_mean",
                          # "6h_vs_8z_from-3m-3s-2m_rnn_coma_unfreeze0.2_mean"
                          ], 
                          label="tl_coma/6h_vs_8z_rnn_coma.png", only_last_legend=True,
                           baseline="baselines/6h_vs_8z_rnn_coma", median=True)