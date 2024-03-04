import numpy as np
from scipy.integrate import trapezoid
from plt_tools import include_plot, load_data

REG_methods = {"trapezoid": trapezoid}


def calculate_auc(model:str,
                  variable:str="battle_won_mean", # variable to calculate the AUC for
                  method:str = "trapezoid"
                  ):
    
    data = load_data(model)

    if variable not in data: raise ValueError(f"Variable {variable} not found in data for model {model}")

    AUC_val = REG_methods[method](data[variable + "_avg"])

    return AUC_val


def auc_ratio(source:str, targets:list, variable:str="battle_won_mean", method:str = "trapezoid", print_results:bool = True):
    AUC_source = calculate_auc(source, variable, method)

    AUC_ratios = []
    for target in targets:
        AUC_target = calculate_auc(target, variable, method)
        AUC_ratios.append((AUC_target - AUC_source) / AUC_target)

    if print_results:
        print("###########################")
        for i, target in enumerate(targets):
            print(f"Source: {source} Target: {target}")
            print(f"AUC_ratio: {AUC_ratios[i]:.3f}")

    return AUC_ratios



ratios = auc_ratio("qmix_3m_baseline", 
                   ["qmix_3m_to_3m_direct", "qmix_3m_to_3m_grad_unfreeze_05"],
           "battle_won_mean", "trapezoid") 

# ratios = auc_ratio("qmix_8m_baseline", 
#                    ["qmix_3m_to_3m_direct", "qmix_3m_to_3m_grad_unfreeze_05"],
#            "battle_won_mean", "trapezoid") 


ratios = auc_ratio("qmix_3m_baseline", 
                   ["qmix_8m_to_3m_direct", 
                    "qmix_8m_to_3m_grad_unfreeze_02",
                    "qmix_8m_to_3m_grad_unfreeze_05",
                    "qmix_8m_to_3m_grad_unfreeze_inf",
                    ],
           "battle_won_mean", "trapezoid") 










