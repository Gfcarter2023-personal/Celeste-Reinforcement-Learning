import moves
import time
import model
import environment
import gym
import actions

moves.initialize()
state = model.State()

x, y = celesteToPCCoordinates(60, 570)
state.findLocation()
print(state.locate())
moves.right(0.5)
state.findLocation(state.locate())
print(state.locate())

def main():
    env = environment.Env()
    for step in range(100000):
        if env.done:
            moves.reset()
        state, reward, done, info = env.step(env.action_space.sample())
    env.close()


