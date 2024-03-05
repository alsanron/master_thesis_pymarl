import torch as th
import torch.nn as nn
import torch.nn.functional as F

class RNNAgent(nn.Module):
    def __init__(self, input_shape, args):
        super(RNNAgent, self).__init__()
        self.args = args

        self.pad = nn.ConstantPad1d((0, 512 - input_shape), 0)

        self.fc1 = nn.Linear(input_shape, args.rnn_hidden_dim)

        # by default num_layers=1, bias=True, batch_first=False
        self.rnn = nn.GRUCell(args.rnn_hidden_dim, args.rnn_hidden_dim)

        self.fc2 = nn.Linear(args.rnn_hidden_dim, args.n_actions)

    def init_hidden(self):
        # make hidden states on same device as model
        return self.fc1.weight.new(1, self.args.rnn_hidden_dim).zero_()

    def forward(self, inputs, hidden_state, freeze_rnn=False):

        for param in self.rnn.parameters():
            param.requires_grad = not freeze_rnn

        inputs_padded = self.pad(inputs)

        x = F.relu(self.fc1(inputs_padded))

        h_in = hidden_state.reshape(-1, self.args.rnn_hidden_dim)
        h = self.rnn(x, h_in)

        q = self.fc2(h)
        return q, h

