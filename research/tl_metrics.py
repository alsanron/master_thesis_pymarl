import numpy as np
from scipy.integrate import trapezoid, cumulative_trapezoid
from plt_tools import load_data

REG_methods = {"trapezoid": trapezoid, "cumulative_trapezoid": cumulative_trapezoid}


def calculate_auc(model:str,
                  variable:str="battle_won_mean", # variable to calculate the AUC for
                  method:str = "cumulative_trapezoid",
                  median:bool=False
                  ):
    
    data = load_data(model, median=median)

    if variable not in data: raise ValueError(f"Variable {variable} not found in data for model {model}")

    if median:
        AUC_val = REG_methods[method](data[variable + "_median"], x=data[variable + "_T"])
    else:
        AUC_val = REG_methods[method](data[variable + "_avg"], x=data[variable + "_T"])

    return AUC_val


def auc_ratio(source:str, targets:list, variable:str="battle_won_mean", method:str = "trapezoid", 
              print_results:bool = True, median:bool=False):
    AUC_source = calculate_auc(source, variable, method, median=median)

    AUC_ratios = []
    for target in targets:
        AUC_target = calculate_auc(target, variable, method, median=median)
        AUC_ratios.append((AUC_target - AUC_source) / AUC_target)

    if print_results:
        print("###########################")
        for i, target in enumerate(targets):
            print(f"Source: {source} Target: {target}")
            print(f"AUC_ratio: {AUC_ratios[i]:.3f}")

    return AUC_ratios











