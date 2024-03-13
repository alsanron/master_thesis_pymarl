from transfer_learning.tools_tl import load_model, extract_layer_params

# Directly transfer the weights from one model to another
def direct_single_transfer_weights(source_model:list, 
                     target_model, # it should be one of the MAC controllers
                     pad_input:bool=False,
                     ):
    th_params = load_model(source_model, timestep=0)

    fc1_params = extract_layer_params(th_params, "fc1")

    gru_params = extract_layer_params(th_params, "rnn")

    if pad_input:
        target_model.agent.fc1.load_state_dict(fc1_params)

    target_model.agent.rnn.load_state_dict(gru_params)

    return target_model



# Directly transfer the weights from one model to another
def direct_multiple_transfer_weights(source_models:list, 
                     target_model, # it should be one of the MAC controllers
                     policy_distillation:str,
                     pad_input:bool=False,
                     ):
    th_params = []; fc1_params = []; gru_params = []
    for model in source_models:
        th_params.append(load_model(model, timestep=0))
        fc1_params.append(extract_layer_params(th_params[-1], "fc1"))
        gru_params.append(extract_layer_params(th_params[-1], "rnn"))

    gru_params_distilled = {}
    if policy_distillation == "mean":
        for key in gru_params[0].keys():
            gru_params_distilled[key] = sum([gru_params[i][key] for i in range(len(gru_params))]) / len(gru_params)
            
    elif policy_distillation == "additive":
        for key in gru_params[0].keys():
            gru_params_distilled[key] = sum([gru_params[i][key] for i in range(len(gru_params))])

    if pad_input:
        raise ValueError("Padding input not supported for multiple transfer learning")
        target_model.agent.fc1.load_state_dict(fc1_params)

    target_model.agent.rnn.load_state_dict(gru_params_distilled)

    return target_model
