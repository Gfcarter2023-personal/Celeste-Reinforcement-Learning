import moves
import time
import model
import environment
import gym
import actions
from PIL import Image

moves.initialize()
x, y = model.celesteToPCCoordinates(60, 570)
state = model.State((x,y))
state.findLocation(state.locate())
print(state.locate())
moves.right(0.2)
state.findLocation(state.locate())
print(state.locate())



def main():
    env = environment.Env()
    for step in range(100000):
        if env.done:
            moves.reset()
        state, reward, done, info = env.step(env.action_space.sample())
    env.close()


