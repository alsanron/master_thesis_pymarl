from transfer_learning.tools_tl import load_model, extract_layer_params

# Directly transfer the weights from one model to another
def direct_transfer_weights(source_model:str, 
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
