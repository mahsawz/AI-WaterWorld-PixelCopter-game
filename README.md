# WaterWorld-PixelCopter-game

In this project, I use PLE module which you can install it [here](https://pygame-learning-environment.readthedocs.io/en/latest/user/home.html) and also this module works on Python2.7

How to use the PLE module:

<img src="https://github.com/mahsawz/WaterWorld-PixelCopter-game/blob/main/PLE-image.png" width="500" height="150">

First, for implementing the "WaterWorld" game, I should consider the game's rule such as:

States:

- player_velocity_y: A float number that indicates the velocity in y axis
- player_velocity_x: A float number that indicates the velocity in x axis
- creep_dist
  - BAD: list of player's distance from red circles
  - GOOD: list of player's distance from green circles
- creep_pos
  - BAD: list of red circles's position
  - GOOD: list of green circles's position
- player_x: player's position in x axis
- player_y: player's position in y axis

Actions:

- 115: go down
- 100: go right
- 119: go up
- 97: go left
- None: stop

<img src="https://github.com/mahsawz/WaterWorld-PixelCopter-game/blob/main/waterworld-image.png" width="200" height="200">

Second, for implementing the "PixelCopter" game, I should consider the game's rule such as:

States:

- player_vel: the player's velocity
- player_dist_to_ceil: A float that indicates the distance to ceil
- next_gate_block_top: lower block's position
- next_gate_block_bottom: upper block's position
- next_gate_dist_to_player: next block's position
- player_dist_to_floor: A float that indicates the distance from ground
- player_y: A float that indicates player's position

Actions:

- 119: go up
- None: don't do anything, and because of gravity, go downs

<img src="https://github.com/mahsawz/WaterWorld-PixelCopter-game/blob/main/pixelcopter-image.png" width="200" height="200">
