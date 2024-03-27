import torch as th
import torch.nn as nn
import torch.nn.functional as F

class TransformerAgent(nn.Module):
    def __init__(self, input_shape, args):
        super(TransformerAgent, self).__init__()
        self.args = args

        self.fc1 = nn.Linear(input_shape, args.d_model)

        self.transformer = nn.Transformer(d_model=args.d_model, 
                                          nhead=args.n_head, 
                                          num_encoder_layers=args.n_encoder_layers, 
                                          num_decoder_layers=args.n_decoder_layers, 
                                          dim_feedforward=args.dim_feedforward, 
                                          dropout=0.1, activation='relu', batch_first=True)
        
        self.fc2 = nn.Linear(args.d_model, args.n_actions)

        # TODO should I initialize weights in a better way?


    def forward(self, inputs):
        x = F.relu(self.fc1(inputs))

        x = self.transformer(x, x)

        q = self.fc2(x)

        return q


