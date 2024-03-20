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

# Drop Rows where there are Nan values.
df = dff.dropna(axis=0, how='any', subset=['Gender', 'Do you consider yourself to be a fan of the Star Trek franchise?',
                                           'Have you seen any of the 6 films in the Star Wars franchise?'])

print("number of rows", df.shape[0])
print("number of columns", df.shape[1])
print("name of columns", df.columns)

# Get domain of single column values.
print("Domain Gender", df['Gender'].unique())
print("Domain Seen Films", df['Have you seen any of the 6 films in the Star Wars franchise?'].unique())
print("Domain Expanded", df['Do you consider yourself to be a fan of the Star Wars film franchise?'].unique())
print("Domain Star Trek Fan", df['Do you consider yourself to be a fan of the Star Trek franchise?'].unique())

# num female.
dfFemale = df.query('Gender==\'Female\'')
pFemale = dfFemale.shape[0] / df.shape[0]

# num not female.
dfNotFemale = df.query('Gender!=\'Female\'')
pNotFemale = dfNotFemale.shape[0] / df.shape[0]

# print(pFemale)
# print(pNotFemale)

# num trek fan | gender calculations
# Female, Fan (T, T)
dfFemTrekFan = df.query("`Gender` == 'Female' and "
                        "`Do you consider yourself to be a fan of the Star Trek franchise?` == 'Yes'")
pFemTrekFan = dfFemTrekFan.shape[0] / df.shape[0]
pTrekFan_Female = pFemTrekFan / pFemale
# print(pTrekFan_Female)
# Female, Not Fan (T, F)
dfFemTrekNotFan = df.query("`Gender` == 'Female' and "
                           "`Do you consider yourself to be a fan of the Star Trek franchise?` != 'Yes'")
pFemTrekNotFan = dfFemTrekNotFan.shape[0] / df.shape[0]
pTrekNotFan_Female = pFemTrekNotFan / pFemale
# print(pTrekNotFan_Female)
# Male, Fan (F, T)
dfMaleTrekFan = df.query("`Gender` == 'Male' and "
                         "`Do you consider yourself to be a fan of the Star Trek franchise?` == 'Yes'")
pMaleTrekFan = dfMaleTrekFan.shape[0] / df.shape[0]
pTrekFan_Male = pMaleTrekFan / pNotFemale
# print(pTrekFan_Male)
# Male, Not Fan (F, F)
dfMaleTrekNotFan = df.query("`Gender` == 'Male' and "
                            "`Do you consider yourself to be a fan of the Star Trek franchise?` != 'Yes'")
pMaleTrekNotFan = dfMaleTrekNotFan.shape[0] / df.shape[0]
pTrekNotFan_Male = pMaleTrekNotFan / pNotFemale
# print(pTrekNotFan_Male)

# num seen star wars | gender
# Female, Seen (T, T)
dfFemSeen = df.query("`Gender` == 'Female' and "
                     "`Have you seen any of the 6 films in the Star Wars franchise?` == 'Yes'")
pFemSeen = dfFemSeen.shape[0] / df.shape[0]
pSeen_Female = pFemSeen / pFemale
# print(pSeen_Female)
# Female, Not Seen (T, F)
dfFemNotSeen = df.query("`Gender` == 'Female' and "
                        "`Have you seen any of the 6 films in the Star Wars franchise?` != 'Yes'")
pFemNotSeen = dfFemNotSeen.shape[0] / df.shape[0]
pNotSeen_Female = pFemNotSeen / pFemale
# print(pNotSeen_Female)
# Male, Seen (F, T)
dfMaleSeen = df.query("`Gender` == 'Male' and "
                      "`Have you seen any of the 6 films in the Star Wars franchise?` == 'Yes'")
pMaleSeen = dfMaleSeen.shape[0] / df.shape[0]
pSeen_Male = pMaleSeen / pNotFemale
# print(pSeen_Male)
# Male, Not Seen (F, F)
dfMaleNotSeen = df.query("`Gender` == 'Male' and "
                         "`Have you seen any of the 6 films in the Star Wars franchise?` != 'Yes'")
pMaleNotSeen = dfMaleNotSeen.shape[0] / df.shape[0]
pNotSeen_Male = pMaleNotSeen / pNotFemale
# print(pNotSeen_Male)

# num fan | seen star wars
# num Seen
dfSeen = df.query("`Have you seen any of the 6 films in the Star Wars franchise?` == 'Yes'")
pSeen = dfSeen.shape[0] / df.shape[0]
# num Not Seen
dfNotSeen = df.query("`Have you seen any of the 6 films in the Star Wars franchise?` == 'No'")
pNotSeen = dfNotSeen.shape[0] / df.shape[0]
# Fan, Seen (T, T)
dfSWFanSeen = df.query("`Do you consider yourself to be a fan of the Star Wars film franchise?` == 'Yes' and "
                       "`Have you seen any of the 6 films in the Star Wars franchise?` == 'Yes'")
pSWFanSeen = dfSWFanSeen.shape[0] / df.shape[0]
pFan_Seen = pSWFanSeen / pSeen
# print(pFan_Seen)
# Fan, Not Seen (T, F)
dfSWFanNotSeen = df.query("`Do you consider yourself to be a fan of the Star Wars film franchise?` == 'Yes' and "
                          "`Have you seen any of the 6 films in the Star Wars franchise?` == 'No'")
pSWFanNotSeen = dfSWFanNotSeen.shape[0] / df.shape[0]
pFan_NotSeen = pSWFanNotSeen / pNotSeen
# print(pFan_NotSeen)
# Not Fan, Seen (F, T)
dfSWNotFanSeen = df.query("`Do you consider yourself to be a fan of the Star Wars film franchise?` == 'No' and "
                          "`Have you seen any of the 6 films in the Star Wars franchise?` == 'Yes'")
pSWNotFanSeen = dfSWNotFanSeen.shape[0] / df.shape[0]
pNotFan_Seen = pSWNotFanSeen / pSeen
# print(pNotFan_Seen)
# Not Fan, Not Seen (F, F)
dfSWNotFanNotSeen = df.query("`Do you consider yourself to be a fan of the Star Wars film franchise?` == 'No' and "
                             "`Have you seen any of the 6 films in the Star Wars franchise?` == 'No'")
pSWNotFanNotSeen = dfSWNotFanNotSeen.shape[0] / df.shape[0]
pNotFan_NotSeen = pSWNotFanNotSeen / pNotSeen
print(pNotFan_NotSeen)

StarWars = BayesNet([
    ('Gender', '', pFemale),
    ('StarTrekFan', 'Gender', {T: pTrekFan_Female, F: pTrekFan_Male}),
    ('SeenStarWars', 'Gender', {T: pSeen_Female, F: pSeen_Male}),
    ('StarWarsFan', 'SeenStarWars', {T: pFan_Seen, F: pFan_NotSeen})
])

print("\n\nEnumerations")
# First Enumeration (Part 1)
print("P(Gender | StarTrekFan = T, StarWarsFan = F) : ",
      enumeration_ask('Gender', dict(StarTrekFan=T, StarWarsFan=T), StarWars).show_approx())

# Second Enumeration (Part 2, and the one I'm using for the rest.)
print("P(StarTrekFan | Gender = T) : ",
      enumeration_ask('StarTrekFan', dict(Gender=T), StarWars).show_approx())

