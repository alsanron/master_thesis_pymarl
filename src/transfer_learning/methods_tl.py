from transfer_learning.tools_tl import load_model, extract_gru_params

# Directly transfer the weights from one model to another
def direct_transfer_weights(source_model:str, 
                     target_model, # it should be one of the MAC controllers
                     ):
    th_params = load_model(source_model, timestep=0)

    gru_params = extract_gru_params(th_params)

    target_model.agent.rnn.load_state_dict(gru_params)

    return target_model
