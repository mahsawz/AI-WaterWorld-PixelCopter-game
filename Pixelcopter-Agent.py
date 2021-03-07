import numpy as np
from ple import PLE
from ple.games.pixelcopter import Pixelcopter
import random


def round(state):
    new_state = {}
    for i in state:
        if i != 'player_y':
            new_state[i] = (int(state[i]) / 60)
    return new_state


# Making an agent from game env
agent = Pixelcopter(width=256, height=256)

# Creating a game environment (use lower fps so we can see whats happening a little easier)
env = PLE(agent, fps=15, force_fps=False, display_screen=True)

env.init()
actions = env.getActionSet()
q_table = {}
alpha = 0.1
gamma = 0.5

while (True):
    oldGameState = round(agent.getGameState())
    if env.game_over():
        env.reset_game()
    up = q_table.get(tuple(oldGameState.values()) + (119,), 0)
    none = q_table.get(tuple(oldGameState.values()) + (None,), 0)

    if up > none:
        action = 119
    elif none > up:
        action = None
    else:
        action = actions[random.randint(0, 1)]  # random actions

    reward = env.act(action)
    newGameState = round(agent.getGameState())
    oldQState = tuple(oldGameState.values()) + (action,)
    if oldQState not in q_table.keys():
        q_table[oldQState] = 0

    up_next = q_table.get(tuple(newGameState.values()) + (119,), 0)
    none_next = q_table.get(tuple(newGameState.values()) + (None,), 0)
    next_max = max(up_next, none_next)
    sample = reward + gamma * next_max
    q_table[oldQState] = (1 - alpha) * q_table[oldQState] + alpha * sample
