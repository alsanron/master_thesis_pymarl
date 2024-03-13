import torch as th
import torch.nn as nn
import torch.nn.functional as F

class TransformerAgent(nn.Module):
    def __init__(self, args):
        super(TransformerAgent, self).__init__()
        self.args = args

        self.transformer = nn.Transformer(d_model=args.rnn_hidden_dim, 
                                          nhead=1, 
                                          num_encoder_layers=1, 
                                          num_decoder_layers=1, 
                                          dim_feedforward=2048, 
                                          dropout=0.1, activation='relu')


    def init_hidden(self):
        # make hidden states on same device as model
        self.transformer._reset_parameters()
        # return self.fc1.weight.new(1, self.args.rnn_hidden_dim).zero_()

    def forward(self, inputs):


        x = self.transformer(inputs, inputs)

        # if freeze_rnn:
        #     with th.no_grad():
        #         h_in = hidden_state.reshape(-1, self.args.rnn_hidden_dim)
        #         h = self.rnn(x, h_in)
        # else:
        #     h_in = hidden_state.reshape(-1, self.args.rnn_hidden_dim)
        #     h = self.rnn(x, h_in)
        a=2

        return 0


