import json
from plt_tools import load_data
from tl_metrics import jumpstart, auc, auc_ratio, asymptotic


def load_config(model_path:str):
    with open("data/" + model_path + "/sacred/1/config.json", "r") as f:
        config = json.load(f)
    return config

def create_csv_line(config, results):
    line = ""

    line += 

model_path = "baselines/3m_rnn_qmix"

config = load_config(model_path)

jumpstart_val = jumpstart(model_path, variable="return_mean", median=True)
asymptotic_val = asymptotic(model_path, variable="return_mean", median=True)
auc_rewards = auc(model_path, variable="return_mean", method="trapezoid", median=True)
auc_bwm = auc(model_path, variable="battle_won_mean", method="trapezoid", median=True)
total_wall_time = asymptotic(model_path, variable="wall_time_min", median=True)

results_grouped = {"jumpstart": jumpstart_val, 
                "asymptotic": asymptotic_val, 
                "auc_rewards": auc_rewards, 
                "auc_bwm": auc_bwm, 
                "total_wall_time": total_wall_time}

print(config)