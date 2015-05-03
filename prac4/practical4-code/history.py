import copy 
class History(object):
  class EpochHistory(object):
    """
    Allows access to the results from previous epochs.
    Copies are made so client can't change the history.
    """
    def __init__(self,rewards,scores,data):
      self.reward = copy.deepcopy(rewards)
      self.scores = copy.deepcopy(scores)
      self.data = copy.deepcopy(data)

  def __init__(self,rewards,scores,data):
    self.epoch = lambda t: History.EpochHistory(
      rewards[t], scores[t], data[t])

    self.last_epoch = lambda: max(rewards.keys())
    self.num_rounds = lambda: max(rewards.keys()) + 1
