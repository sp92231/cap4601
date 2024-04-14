"""
Name: Shanie Portal
Date: 04/08/2024
Assignment: Module 11: Project - MDP
Due Date: 04/07/2024
About this project: Salmon fishing this year, calculated through MDP, Value, and Policy Iteration.
Assumptions:NA
All work below was performed by Shanie Portal. Closely followed Dr. Works' Videos. """

import mdptoolbox
import numpy as np

##########################
# The number of states
STATES = 4
# The number of actions
ACTIONS = 2
ACTION_FISH = 0
ACTION_NULL = 1

# P[0] = Fish
P = np.array([
    # P[0] = Fish
    [[1, 0, 0, 0],  # 0 = Empty
     [.75, .25, 0, 0],  # 1 = Low
     [0, .75, .25, 0],  # 2 = Medium
     [0, 0, .60, .40]],  # 3 = High
    # P[1] = Null
    [[0, 1, 0, 0],  # 0 = Empty
     [0, .30, .70, 0],  # 1 = Low
     [0, 0, .25, .75],  # 2 = Medium
     [0, 0, .05, .95]]  # 3 = High
])

# [0] = Fish
# [1] = Null
R = np.array([[0, -200000],
              [5000, 0],
              [50000, 0],
              [100000, 0]])

print("P=", P)
print("R=", R)

Discount = 0.9
NumPeriods = 10

##########################
print("Value Iteration")
vi = mdptoolbox.mdp.ValueIteration(P, R, Discount, NumPeriods)
vi.setVerbose()
vi.run()
print("optimal value function=", vi.V)
print("optimal policy=", vi.policy)
##########################

##########################
print("Policy Iteration")
pi = mdptoolbox.mdp.PolicyIteration(P, R, Discount)
pi.setVerbose()
pi.run()
print("optimal value function=", pi.V)
print("optimal policy=", pi.policy)
##########################
