"""
Name: Shanie Portal
Date: 03/24/2024
Assignment: Module 9: Project - MM and HMM
Due Date: 03/24/2024
About this project: HMM and MM around a specific dataset
Assumptions:NA
All work below was performed by Shanie Portal. Heavily followed Dr. Works' videos.
"""
import random
import pandas as pd
import numpy as np
from MarkovChain import *
from MChainDraw import *
from statistics import mean
from probability import *
from utils import rounder

random.seed("aima-python")
file = r"PRSA_Data_Tiantan_20130301-20170228.csv"
df = pd.read_csv(file)

# print(df)
# print(df['TEMP'].unique())
# print(df['TEMP'].dtype)
print("min = ", min(df["TEMP"]))
print("max = ", max(df["TEMP"]))
print("mean = ", df["TEMP"].mean())

