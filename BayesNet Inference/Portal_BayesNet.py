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

