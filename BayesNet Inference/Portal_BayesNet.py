"""
Name: Shanie Portal
Date: 03/15/24
Assignment: Module 8: Project - BayesNet Inference and Sampling
Due Date: 03/17/24
About this project: BayesNet Inference and Sampling Probability Analysis of the Star Wars Survey.
Assumptions: N/A
All work below was performed by Shanie Portal
"""

from BayesNet import *
import random
import pandas as pd
import numpy as np

random.seed("aima-python")

T, F = True, False

file = r"StarWars.xlsx"
dff = pd.read_excel(file)

