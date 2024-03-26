import json
import numpy as np
import pandas as pd
import os
from plt_tools import load_data
from tl_metrics import jumpstart, auc, auc_ratio, asymptotic


def load_config(model:str):
    with open(model + "/sacred/2/config.json", "r") as f:
        config = json.load(f)
    return config

def load_results(model:str):
    jumpstart_val = jumpstart(model, variable="return_mean", median=True)
    asymptotic_val = asymptotic(model, variable="return_mean", median=True)
    auc_rewards = auc(model, variable="return_mean", method="trapezoid", median=True)
    auc_bwm = auc(model, variable="battle_won_mean", method="trapezoid", median=True)
    total_wall_time = asymptotic(model, variable="wall_time_min", median=True)

    results_grouped = {"initial_rewards": jumpstart_val, 
                "asymptotic_rewards": asymptotic_val, 
                "auc_rewards": auc_rewards, 
                "auc_bwm": auc_bwm, 
                "total_wall_time": total_wall_time}
    return results_grouped

def create_csv_line(model:str, baseline:str):
    # Load the results from the model and baseline
    config = load_config(model)
    results = load_results(model)

    baseline_results = load_results("data/baselines/" +  baseline)
    baseline_config = load_config("data/baselines/" + baseline)

    line = "{},".format(config["label"])

    line += "{:.2f},".format(results["initial_rewards"])
    line += "{:.2f},".format(results["asymptotic_rewards"])
    line += "{:.2f},".format(results["auc_rewards"])
    line += "{:.2f},".format(results["auc_bwm"])
    line += "{:.2f},".format((results["auc_rewards"] - baseline_results["auc_rewards"])/(results["auc_rewards"] + 1e-6))
    line += "{:.2f},".format((results["auc_bwm"] - baseline_results["auc_bwm"])/(results["auc_bwm"] + 1e-6))
    line += "{:.2f}\r\n".format(results["total_wall_time"])

    return line

def generate_results(list_to_process):
    
    csv_results = ""

    for key in list_to_process.keys():
        model = key
        baseline = list_to_process[key]
        line_csv = create_csv_line(model=model, baseline=baseline)
        csv_results += line_csv

    with open("new_results.csv", "w") as f:
        f.write(csv_results)

def generate_results_from_folder(folder_with_data:str, baseline:str):
    list_to_process = {}
    for file in os.listdir("data/" + folder_with_data):
        file_path = "data/" + folder_with_data + "/" + file
        if os.path.isdir(file_path):
            list_to_process[file_path] = baseline

    generate_results(list_to_process)


list_to_process = {
    "data/baselines/25m_rnn_coma": "3m_rnn_coma",
    "data/baselines/25m_rnn_qmix": "3m_rnn_coma",
    "data/baselines/2m_vs_1z_rnn_coma": "3m_rnn_coma",
    "data/baselines/2m_vs_1z_rnn_qmix": "3m_rnn_coma",
    "data/baselines/2s3z_rnn_coma": "3m_rnn_coma",
    "data/baselines/2s3z_rnn_qmix": "3m_rnn_coma",
    "data/baselines/3m_rnn_coma": "3m_rnn_coma",
    "data/baselines/3m_rnn_qmix": "3m_rnn_coma",
    "data/baselines/3s5z_rnn_coma": "3m_rnn_coma",
    "data/baselines/3s5z_rnn_qmix": "3m_rnn_coma",
    "data/baselines/3s_vs_3z_rnn_coma": "3m_rnn_coma",
    "data/baselines/3s_vs_3z_rnn_qmix": "3m_rnn_coma",
    "data/baselines/3s_vs_4z_rnn_coma": "3m_rnn_coma",
    "data/baselines/3s_vs_4z_rnn_qmix": "3m_rnn_coma",
    "data/baselines/5m_vs_6m_rnn_coma": "3m_rnn_coma",
    "data/baselines/5m_vs_6m_rnn_qmix": "3m_rnn_coma",
    "data/baselines/6h_vs_8z_rnn_coma": "3m_rnn_coma",
    "data/baselines/6h_vs_8z_rnn_qmix": "3m_rnn_coma",
    "data/baselines/8m_rnn_coma": "3m_rnn_coma",
    "data/baselines/8m_rnn_qmix": "3m_rnn_coma"
}


generate_results_from_folder("transfer_qmix/8m_from_3m_gridsearch", "8m_rnn_qmix")
