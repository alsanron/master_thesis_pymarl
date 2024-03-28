from modules.agents import REGISTRY as agent_REGISTRY
from components.action_selectors import REGISTRY as action_REGISTRY
import torch as th

# This multi-agent controller shares parameters between agents. It is very similar to BasicMAC, but
# has been modified to be able to work with Transformers
class BasicMACTransformer:
    def __init__(self, scheme, groups, args):
        self.n_agents = args.n_agents
        self.args = args
        input_shape = self._get_input_shape(scheme)
        self._build_agents(input_shape)
        self.agent_output_type = args.agent_output_type

        self.action_selector = action_REGISTRY[args.action_selector](args)

    def select_actions(self, ep_batch, t_ep, t_env, bs=slice(None), test_mode=False):
        avail_actions = th.movedim(ep_batch["avail_actions"][:, :t_ep+1], 2, 1)

        agent_outputs = self.forward(ep_batch, t_ep, test_mode=test_mode)

        chosen_actions = self.action_selector.select_action(agent_outputs[bs], avail_actions[bs], t_env, test_mode=test_mode)

        # selects the action associated to the last timestep
        chosen_actions = chosen_actions[:, :, -1] 

        return chosen_actions

    def forward(self, ep_batch, t, test_mode=False, freeze_rnn=False):
        # TODO remove this freeze_rnn from here
        agent_inputs = self._build_inputs(ep_batch, t)

        if t == -1:
            agent_outs = self.agent(agent_inputs, causal=True)
            agent_outs = th.movedim(agent_outs.view(ep_batch.batch_size, self.n_agents, ep_batch.max_seq_length, -1), 2, 1)
        else:
            agent_outs = self.agent(agent_inputs)
            agent_outs = agent_outs.view(ep_batch.batch_size, self.n_agents, t+1, -1) # redo the reshaping

        return agent_outs

    def init_hidden(self, batch_size):
        # just for legacy usage
        pass

    def parameters(self):
        return self.agent.parameters()

    def load_state(self, other_mac):
        self.agent.load_state_dict(other_mac.agent.state_dict())

    def cuda(self):
        self.agent.cuda()

    def save_models(self, path):
        th.save(self.agent.state_dict(), "{}/agent.th".format(path))

    def load_models(self, path):
        self.agent.load_state_dict(th.load("{}/agent.th".format(path), map_location=lambda storage, loc: storage))

    def _build_agents(self, input_shape):
        self.agent = agent_REGISTRY[self.args.agent](input_shape, self.args)

    def _build_inputs(self, batch, t=-1):
        # Assumes homogenous agents with flat observations.
        # Other MACs might want to e.g. delegate building inputs to each agent
        bs = batch.batch_size
        inputs = []

        if t == -1: # then we parse the whole batch of sequences at once, applying causal mask
            inputs.append(batch["obs"])  # considers the whole sequence of inputs until current ts

            if self.args.obs_last_action:
                # inputs actions taken in prevous timesteps. Current timestemp actions are
                inputs.append(batch["actions_onehot"])

            if self.args.obs_agent_id:
                inputs.append(th.eye(self.n_agents, device=batch.device).unsqueeze(0).expand(bs, batch.max_seq_length, -1, -1))

            inputs = [th.movedim(x, 2, 1) for x in inputs] # move number of agents to second dimension
            inputs = th.cat([x.reshape(bs*self.n_agents, batch.max_seq_length, -1) for x in inputs], dim=2)

        else:
            inputs.append(batch["obs"][:, :(t+1)])  # considers the whole sequence of inputs until current ts

            if self.args.obs_last_action:
                zeros_array = th.zeros_like(batch["actions_onehot"][:, t]).unsqueeze(1)
                if t == 0:
                    inputs.append(zeros_array)
                else:
                    # inputs actions taken in prevous timesteps. Current timestemp actions are
                    inputs.append(th.cat([batch["actions_onehot"][:, :t], zeros_array], dim=1))

            if self.args.obs_agent_id:
                inputs.append(th.eye(self.n_agents, device=batch.device).unsqueeze(0).expand(bs, t+1, -1, -1))

            inputs = [th.movedim(x, 2, 1) for x in inputs] # move number of agents to second dimension

            # bs*self.n_agents may be kept, as observations drawn for each agent do not have to change
            inputs = th.cat([x.reshape(bs*self.n_agents, t+1, -1) for x in inputs], dim=2)


        return inputs

    def _get_input_shape(self, scheme):
        input_shape = scheme["obs"]["vshape"]
        if self.args.obs_last_action:
            input_shape += scheme["actions_onehot"]["vshape"][0]
        if self.args.obs_agent_id:
            input_shape += self.n_agents

        return input_shape
