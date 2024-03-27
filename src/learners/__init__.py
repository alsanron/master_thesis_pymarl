from .q_learner import QLearner
from .q_learner_transformer import QLearnerTransformer
from .coma_learner import COMALearner

REGISTRY = {}

REGISTRY["q_learner"] = QLearner
REGISTRY["coma_learner"] = COMALearner
REGISTRY["q_learner_transformer"] = QLearnerTransformer
