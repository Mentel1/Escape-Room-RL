"""play a game and see it on terminal"""

import os
import sys
import keyboard

from Environment import EscapeRoomEnvironment
from constants import env_params

env = EscapeRoomEnvironment(env_params=env_params)
env.start()

key_to_action = {"haut": 0, "gauche": 1, "bas": 2, "droite": 3}

# iterate
while True:
    os.system("cls")
    sys.stdout.write(env.render())
    event = keyboard.read_event()
    if event.event_type == keyboard.KEY_DOWN and event.name in key_to_action:
        action = key_to_action[event.name]
        reward, state, term = env.step(action)
        if term:
            # render final frame
            sys.stdout.write(env.render())
            break
