#!/usr/bin/env python3
import random
import gym
import gym.spaces
import gym.wrappers
import gym.envs.toy_text.frozen_lake
from collections import namedtuple
import numpy as np
from tensorboardX import SummaryWriter

import torch
import torch.nn as nn
import torch.optim as optim

if __name__ == "__main__":

    env_name = "FrozenLake-v0"
    e = gym.make(env_name)

    print(e.observation_space)
    print(e.action_space)
    print(e.reset())
    print(e.render())