import numpy as np
from ple import PLE
from ple.games.waterworld import WaterWorld
import random
import operator


def round(state):
    new_state = {}

    for i in state:
        if i != 'creep_pos' and i != 'player_x' and i != 'player_y':
            if i == 'creep_dist':
                new_state['creep_dist_BAD'] = tuple(
                    x // 200 for x in state['creep_dist']['BAD'])
                new_state['creep_dist_GOOD'] = tuple(
                    x // 200 for x in state['creep_dist']['GOOD'])
                pass
            else:
                new_state[i] = int(state[i] / 100)
    return new_state


# Making an agent from game env
agent = WaterWorld(width=256, height=256, num_creeps=8)

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

    right = q_table.get(tuple(oldGameState.values()) + (100,), 0)
    left = q_table.get(tuple(oldGameState.values()) + (97,), 0)
    up = q_table.get(tuple(oldGameState.values()) + (119,), 0)
    down = q_table.get(tuple(oldGameState.values()) + (115,), 0)
    none = q_table.get(tuple(oldGameState.values()) + (None,), 0)
    stats = {119: up, 115: down, right: 100, 97: left, None: none}
    if (up == down == none == right == left):
        action = actions[random.randint(0, 4)]  # random actions
    else:
        action = max(stats.items(), key=operator.itemgetter(1))[0]
    reward = env.act(action)
    newGameState = round(agent.getGameState())
    oldQState = tuple(oldGameState.values()) + (action,)
    if oldQState not in q_table.keys():
        q_table[oldQState] = 0

    right_next = q_table.get(tuple(newGameState.values()) + (100,), 0)
    left_next = q_table.get(tuple(newGameState.values()) + (97,), 0)
    up_next = q_table.get(tuple(newGameState.values()) + (119,), 0)
    down_next = q_table.get(tuple(newGameState.values()) + (115,), 0)
    none_next = q_table.get(tuple(newGameState.values()) + (None,), 0)
    next_max = max(up_next, down_next, none_next, left_next, right_next)
    sample = reward + gamma * next_max
    q_table[oldQState] = (1 - alpha) * q_table[oldQState] + alpha * sample
