import model
class Env:
    def __init__(self):
        self.state = model.State()
        self.reward = self.state.giveReward()
        self.done = self.isDone()
        self.info = None

    def isDone(self):
        if self.reward < 0:
            return True
        else:
            return False

    def step(self):
        return 1

    def action_space(self):
