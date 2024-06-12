import moves
import time
import model
import environment

moves.initialize()
state = model.State()

def main():
    env = environment.Env()
    for step in range(100000):
        if env.done:
            moves.reset()
        state, reward, done, info = env.step(env.action_space.sample())
    env.close()


