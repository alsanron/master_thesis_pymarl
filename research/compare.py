import json
import matplotlib.pyplot as plt


def listOfDict_to_listOfValues(input:list) -> list:
    return [d["value"] for d in input]

def include_plot(figure, x_mean, y_mean, x_std=[], y_std=[], label=""):
    plt.figure(figure)
    try:
        y_tmp = listOfDict_to_listOfValues(y_mean) 
        y_mean = y_tmp
        y_std = listOfDict_to_listOfValues(y_std)
    except:
        pass

    plt.plot(x_mean, y_mean, label=label)

    if x_std and y_std:
        plt.fill_between(x_std, 
                         y_mean - y_std, 
                         y_mean + y_std, 
                         alpha=0.3)
        
def generate_plot(variable:str, models:list, with_std:bool = False, save_as:str = None) -> plt.Figure:
    fig = plt.figure()
    for model in models:
        data = json.load(open("data/" + model + "/sacred/info.json"))

        if with_std:
            include_plot(fig, data[variable + '_mean_T'], data[variable + '_mean'], data[variable + '_std_T'], data[variable + '_std'], label=model)
        else:
            include_plot(fig, data[variable + "_T"], data[variable], label=model)
    plt.grid()
    plt.xlabel('Timesteps')
    plt.ylabel(variable)
    plt.legend()

    if save_as:
        plt.savefig("figures/" + save_as)
    return fig


generate_plot('battle_won_mean', ['3m_qmix_baseline', '3m_qmix_4env', '3m_qmix_8env'], with_std=False, save_as='battle_won_mean.png')

generate_plot('return_mean', ['3m_qmix_baseline', '3m_qmix_4env', '3m_qmix_8env'], with_std=False, save_as='return_mean.png')

