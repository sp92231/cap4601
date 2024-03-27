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

def label_temp(row):
    if row['TEMP'] < 16.8:
        return "Cold" # Temperatures below 16.8 deg.
    elif 16.8 <= row['TEMP'] <= 24.0:
        return "Cool" # Temperatures from 16.8 to 24.0 deg.
    elif 24.0 < row['TEMP'] <= 32.0:
        return "Warm" # Temperatures from 24.0 to 32.0 deg.
    elif 32.0 < row['TEMP'] <= 41.1:
        return "Hot" # Temperatures from 32.0 to 41.1 deg.

df['label_temp'] = df.apply(lambda row: label_temp(row), axis=1)
# print(df['label_temp'])

# Initialising variables.
CountColdCold = 0
CountColdCool = 0
CountColdWarm = 0
CountColdHot = 0
CountCoolCold = 0
CountCoolCool = 0
CountCoolWarm = 0
CountCoolHot = 0
CountWarmCold = 0
CountWarmCool = 0
CountWarmWarm = 0
CountWarmHot = 0
CountHotCold = 0
CountHotCool = 0
CountHotWarm = 0
CountHotHot = 0

# Counts.
indxTempLabel = df.columns.get_loc("label_temp")
for i in range(1, df.shape[0] - 1):
    if df.iat[i, indxTempLabel] == 'Cold':
        if df.iat[i + 1, indxTempLabel] == 'Cold':
            CountColdCold += 1
        elif df.iat[i + 1, indxTempLabel] == 'Cool':
            CountColdCool += 1
        elif df.iat[i + 1, indxTempLabel] == 'Warm':
            CountColdWarm += 1
        elif df.iat[i + 1, indxTempLabel] == 'Hot':
            CountColdHot += 1
    elif df.iat[i, indxTempLabel] == 'Cool':
        if df.iat[i + 1, indxTempLabel] == 'Cold':
            CountCoolCold += 1
        elif df.iat[i + 1, indxTempLabel] == 'Cool':
            CountCoolCool += 1
        elif df.iat[i + 1, indxTempLabel] == 'Warm':
            CountCoolWarm += 1
        elif df.iat[i + 1, indxTempLabel] == 'Hot':
            CountCoolHot += 1
    elif df.iat[i, indxTempLabel] == 'Warm':
        if df.iat[i + 1, indxTempLabel] == 'Cold':
            CountWarmCold += 1
        elif df.iat[i + 1, indxTempLabel] == 'Cool':
            CountWarmCool += 1
        elif df.iat[i + 1, indxTempLabel] == 'Warm':
            CountWarmWarm += 1
        elif df.iat[i + 1, indxTempLabel] == 'Hot':
            CountWarmHot += 1
    elif df.iat[i, indxTempLabel] == 'Hot':
        if df.iat[i + 1, indxTempLabel] == 'Cold':
            CountHotCold += 1
        elif df.iat[i + 1, indxTempLabel] == 'Cool':
            CountHotCool += 1
        elif df.iat[i + 1, indxTempLabel] == 'Warm':
            CountHotWarm += 1
        elif df.iat[i + 1, indxTempLabel] == 'Hot':
            CountHotHot += 1

# Probability of Cold.
ProbColdCold = CountColdCold / (CountColdCold + CountColdCool + CountColdWarm +
CountColdHot)
ProbColdCool = CountColdCool / (CountColdCold + CountColdCool + CountColdWarm +
CountColdHot)
ProbColdWarm = CountColdWarm / (CountColdCold + CountColdCool + CountColdWarm +
CountColdHot)
ProbColdHot = CountColdHot / (CountColdCold + CountColdCool + CountColdWarm +
CountColdHot)

# Probability of Cool.
ProbCoolCold = CountCoolCold / (CountCoolCold + CountCoolCool + CountCoolWarm +
CountCoolHot)
ProbCoolCool = CountCoolCool / (CountCoolCold + CountCoolCool + CountCoolWarm +
CountCoolHot)
ProbCoolWarm = CountCoolWarm / (CountCoolCold + CountCoolCool + CountCoolWarm +
CountCoolHot)
ProbCoolHot = CountCoolHot / (CountCoolCold + CountCoolCool + CountCoolWarm +
CountCoolHot)

# Probability of Warm.
ProbWarmCold = CountWarmCold / (CountWarmCold + CountWarmCool + CountWarmWarm +
CountWarmHot)
ProbWarmCool = CountWarmCool / (CountWarmCold + CountWarmCool + CountWarmWarm +
CountWarmHot)
ProbWarmWarm = CountWarmWarm / (CountWarmCold + CountWarmCool + CountWarmWarm +
CountWarmHot)
ProbWarmHot = CountWarmHot / (CountWarmCold + CountWarmCool + CountWarmWarm +
CountWarmHot)

# Probability of Hot.
ProbHotCold = CountHotCold / (CountHotCold + CountHotCool + CountHotWarm +
CountHotHot)
ProbHotCool = CountHotCool / (CountHotCold + CountHotCool + CountHotWarm +
CountHotHot)
ProbHotWarm = CountHotWarm / (CountHotCold + CountHotCool + CountHotWarm +
CountHotHot)
ProbHotHot = CountHotHot / (CountHotCold + CountHotCool + CountHotWarm +
CountHotHot)

transition_prob = {
    'Cold': {
        'Cold': ProbColdCold,
        'Cool': ProbColdCool,
        'Warm': ProbColdWarm,
        'Hot': ProbColdHot
    },
    'Cool': {
        'Cold': ProbCoolCold,
        'Cool': ProbCoolCool,
        'Warm': ProbCoolWarm,
        'Hot': ProbCoolHot
    },
    'Warm': {
        'Cold': ProbWarmCold,
        'Cool': ProbWarmCool,
        'Warm': ProbWarmWarm,
        'Hot': ProbWarmHot
    },
    'Hot': {
        'Cold': ProbHotCold,
        'Cool': ProbHotCool,
        'Warm': ProbHotWarm,
        'Hot': ProbHotHot
    }
}

temp_chain = MarkovChain(transition_prob=transition_prob)
# print(temp_chain.__dict__)

# Generating states
print("\nMarkov States (I add a few since current_state Cold mostly defaults to "
 "Cold since the probability of being cold on a cold day is 98%).\n")
print(temp_chain.next_state(current_state='Cold'))
print(temp_chain.next_state(current_state='Cool'))
print(temp_chain.next_state(current_state='Warm'))
print(temp_chain.next_state(current_state='Hot'))
print(temp_chain.generate_states(current_state='Cold', no=25))
print(temp_chain.generate_states(current_state='Cool', no=25))
print(temp_chain.generate_states(current_state='Warm', no=25))
print(temp_chain.generate_states(current_state='Hot', no=25))

# Importing MarkovChain class.
P = np.array([
 [round(ProbColdCold, 2), round(ProbColdCool, 2), round(ProbColdWarm, 2),
round(ProbColdHot, 2)],
 [round(ProbCoolCold, 2), round(ProbCoolCool, 2), round(ProbCoolWarm, 2),
round(ProbCoolHot, 2)],
 [round(ProbWarmCold, 2), round(ProbWarmCool, 2), round(ProbWarmWarm, 2),
round(ProbWarmHot, 2)],
 [round(ProbHotCold, 2), round(ProbHotCool, 2), round(ProbHotWarm, 2),
round(ProbHotHot, 2)]
])

