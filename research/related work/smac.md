- SMAC based on starcraft-II
- Each unit is controlled by an independent, learning agent that has to act based on local observations. Opponent's units are controlled by hand-coded built-in AI
- Partial observable and high dimensional scenarios
- Pymarl is the learning framework: modular, extensible built on pytorch
- Centralized training with decentralized execution: the learning algorithm has access to all local action-observation histories τ and global state s, but each agent’s learnt policy can condition only on its own action-observation history τ_a

**Some scenarios:**

3 Marines each

[0d643afa84cbd818a62e436738b1c3e4.png](file:///home/alsanron/.config/joplin-desktop/resources/ae9c3122f2284010a1e474667fd35bbc.png)


25 Marines each

![9d1bb5028615db454e92f008fea06979.png](file:///home/alsanron/.config/joplin-desktop/resources/f54f1bb5cbdf4f1aba5d56a2180a7bd7.png)

3 Stalkers & 5 Zealots

![8eb0dfdb8192f7d496de0c2fd63de130.png](file:///home/alsanron/.config/joplin-desktop/resources/68e7ce9e5c9f4366bc7e028660fb905a.png)

1 Medivac, 2 Marauders & 7 Marines each

![edffead069863b50881a0a38ffff8d1c.png](file:///home/alsanron/.config/joplin-desktop/resources/ddba88d6c89b4721b68b5da9ed2bebb2.png)

2 Marines vs 1 Zealot

![20de6a6904afaaf7b0f3e769f2ad8ce5.png](file:///home/alsanron/.config/joplin-desktop/resources/8336059478924c70b20750bde3b38185.png)

2 Stalkers vs 1 Spine Crawler

![0875b4a74ca78022e9c4e51c6d6aceb4.png](file:///home/alsanron/.config/joplin-desktop/resources/b82d5eaaef484730938de0ce92601adb.png)

20 Zerglings & 4 Banelings each

![dee3dcfb9975a9abf285fc0d5784971a.png](file:///home/alsanron/.config/joplin-desktop/resources/5e272375546a4d0f8bfd44bca3fb0cec.png)

2 Colossi vs 64 Zerglings

![8f176486b9a6403f1bd8f27f7da22b27.png](file:///home/alsanron/.config/joplin-desktop/resources/3f4d539fcfdc44f3a598e66083e05d54.png)

## Strategies

The main idea is to maximize damage dealt to enemy units while minimizing damage received.

- **Focus firing:** all the units try to kill the same unit first.
- **Avoid overkill**: avoiding inflicting more damage to units than is necessary to kill them
- Assembling units into formations based on their armor types
- **Kiting**: making enemy units give chase
- Coordinating the positioning of units to attack from different directions
- Taking advantage of the terrain

## State, observations and action space

- An agent receives local observations drawn within its field of view (e.g., 1:36, 3s\_vs\_5z)
- State vector of each agent: distance, relative x, relative y, health, shield, unit\_type and last\_action (only for allies) + height and walkability of 8 terrain points
- All features are normalized by their maximum values
- During training, agents have access to the global state: coordinates of all agents, energy and cooldowns
- Sight range is set to 9, shooting to 6 -> agents need to move before beginning shooting
- Allowed set of actions:
    - move\[{east, west, south, north}\]
    - attack\[enemy_id\]
    - stop
    - no-op(dead agents can only take this action)
    - heal\[enemy_id\] (only healers = medivacs)
- Number of actions ranges between 7 and 70

## Training

- Similar procedure to that in [[qmix.pdf]]
- Training paused after 1e4 timesteps, during which 32 test episodes agents act greedily in a decentralised fashion. Test win rate.
- Agents are training individually. The show the necessity of including an agent's action-observation history to feed an RNN.

## Benchmark

- In SMAC, they master all scenarios with QMIX
- COMA: actor-critic algorithm with a special multi-agent critic baseline. QMIX belongs to the Q-learning family. All other algorithms except COMA are more sample efficient (off-policy value-based methods over on-policy gradient).

## Evaluation guidelines

- Micro scenarios aim to evaluate how well independent agents are able to learn coordination to solve complex tasks. At least 1 micromanagement strategy is required to success.
- Game ends either when all units of either team have died or a pre-specified time limit is reached.
- Overall goal: maximize the win rate for each battle scenario
- Two options for rewards:
    - Shaped reward: based on hit-point damage dealt, enemy units killed + a bonus for winning the battle.
    - Sparse reward: +1/-1 for winning/losing an episode
    - It's a good idea to keep it as default
- QMIX/COMA as state of the art methods, + VDN/IQL as baselines

## Limitations/deficiencies of SMAC

They show that SMAC is insufficiently stochastic to require complex closed-loop policies.

- They train QMIX and MAPPO on open-loop policies, that is, policies conditioned only on the timestep without giving the usual SMAC observation as input. In general, open-loop performs quite bad compared to the close-loop version, but still achieves high and non-trivial win rates.
- It lacks stochasticity