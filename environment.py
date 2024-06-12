from gym import Env
from gym.spaces import Discrete, Box
import numpy as np
import random
import model

class SpecialEnv(Env):
    def __init__(self, state):
        #Actions we can take
        self.action_space = Discrete(26)
        # State array
        self.observation_space = [Box(low=np.arras([0], high=np.array([3840]))), Box(low=np.arras([0], high=np.array([2160])))]
        # Set start state
        self.state = state.findLocation()
        # Set play length
        self.length = 60

    def step(self, action, state):
        # Apply Action
        if action.contains('jump'):
            doJump = True
        if action.contains('dash'):
            doDash = True
        self.state = state.findLocation()
        self.length -= 1
        reward = state.giveReward()

        if self.length <=0:
            done = True
        else:
            done = False
        info = {}
        return self.state, reward, done, info

    def reset(self, state):
        # Resets the state
        self.state = state.findLocation()
        self.length = 60
        return self.state