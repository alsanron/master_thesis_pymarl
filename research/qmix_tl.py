from main_plot import generate_training_figure


############ BLOCK 1 ############
generate_training_figure(["3m_rnn_qmix", "3m_from-3m_rnn_qmix_unfreeze0.2", "3m_from-8m_rnn_qmix_unfreeze0.2",
                          "3m_from-25m_rnn_qmix_unfreeze0.2", 
                        #   "3m_from-5m_rnn_qmix_unfreeze0.2" # currently it doesnt train properly
                          ], label="tl_qmix/3m_rnn_qmix.png", 
                          only_last_legend=True, baseline="3m_rnn_qmix", median=True)

generate_training_figure(["3m_rnn_qmix", "3m_from-2s3z_rnn_qmix_unfreeze0.2", "3m_from-3s_rnn_qmix_unfreeze0.2",
                          "3m_from-2m_rnn_qmix_unfreeze0.2"], label="tl_qmix/3m_rnn_qmix_ext.png", 
                          only_last_legend=True, baseline="3m_rnn_qmix", median=True)

generate_training_figure(["8m_rnn_qmix", "8m_from-3m_rnn_qmix_unfreeze0.2", 
                          "8m_from-8m_rnn_qmix_unfreeze0.2",
                          "8m_from-25m_rnn_qmix_unfreeze0.2", 
                        #   "8m_from-5m_rnn_qmix_direct"
                          ], 
                          label="tl_qmix/8m_rnn_qmix.png", only_last_legend=True, baseline="8m_rnn_qmix", median=True)


generate_training_figure(["25m_rnn_qmix", "25m_from-3m_rnn_qmix_unfreeze0.2", "25m_from-8m_rnn_qmix_unfreeze0.2",
                          "25m_from-25m_rnn_qmix_direct", 
                        #   "25m_from-25m_rnn_qmix_unfreeze0.2",
                        #   "25m_from-5m_rnn_qmix_direct"
                          ], label="tl_qmix/25m_rnn_qmix.png", only_last_legend=True, baseline="25m_rnn_qmix", median=True)


generate_training_figure(["5m_vs_6m_rnn_qmix", "5m_vs_6m_rnn_qmix_ext", "5m_vs_6m_from-3m_rnn_qmix_unfreeze0.2", 
                          "5m_vs_6m_from-8m_rnn_qmix_unfreeze0.2",
                          "5m_vs_6m_from-25m_rnn_qmix_unfreeze0.2", "5m_vs_6m_from-5m_rnn_qmix_unfreeze0.2",
                          ], label="tl_qmix/5m_vs_6m_rnn_qmix.png", 
                          only_last_legend=True, baseline="5m_vs_6m_rnn_qmix", median=True)



############ BLOCK 2 ############
generate_training_figure(["2s3z_rnn_qmix", "2s3z_from-3m_rnn_qmix_unfreeze0.2", "2s3z_from-3s5z_rnn_qmix_unfreeze0.2",
                          ], label="tl_qmix/2s3z_rnn_qmix.png", only_last_legend=True, 
                          baseline="2s3z_rnn_qmix", median=True)

generate_training_figure(["3s5z_rnn_qmix", "3s5z_from-2s3z_rnn_qmix_unfreeze0.2",
                          ], label="tl_qmix/3s5z_rnn_qmix.png", 
                          only_last_legend=True, baseline="3s5z_rnn_qmix", median=True)

############ BLOCK 3 ############

generate_training_figure(["3s_vs_3z_rnn_qmix", "3s_vs_3z_from-3m_rnn_qmix_unfreeze0.2", "3s_vs_3z_from-3s_rnn_qmix_unfreeze0.2",
                          ], label="tl_qmix/3s_vs_3z_rnn_qmix.png", 
                          only_last_legend=True, baseline="3s_vs_3z_rnn_qmix", median=True)

generate_training_figure(["3s_vs_4z_rnn_qmix", 
                        #   "3s_vs_4z_from-3s_rnn_qmix_direct", 
                          "3s_vs_4z_from-3s_rnn_qmix_unfreeze0.2",
                          ], label="tl_qmix/3s_vs_4z_rnn_qmix.png", 
                          only_last_legend=True, baseline="3s_vs_4z_rnn_qmix", median=True)


############ BLOCK 4 ############
generate_training_figure(["2m_vs_1z_rnn_qmix", "2m_vs_1z_from-3m_rnn_qmix_unfreeze0.2",
                          ], label="tl_qmix/2m_vs_1z_rnn_qmix.png", 
                          only_last_legend=True, baseline="2m_vs_1z_rnn_qmix", median=True)

############ BLOCK 5 ############
generate_training_figure(["6h_vs_8z_rnn_qmix", "6h_vs_8z_rnn_qmix_ext", "6h_vs_8z_from-2m_rnn_qmix_direct", 
                          "6h_vs_8z_from-3s_rnn_qmix_direct"], 
                          label="tl_qmix/6h_vs_8z_rnn_qmix.png", only_last_legend=True, median=True)