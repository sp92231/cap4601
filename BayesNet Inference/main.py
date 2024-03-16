"""
Name:Shanie Portal
Date: 03/15/24
Assignment: Module 8: Project - BayesNet Inference and Sampling
Due Date: 03/17/24
About this project: This project implements a Bayesian network in Python for probabilistic inference and sampling.
Assumptions: Valid user input for evidence and acyclicity of the Bayesian network.
All work below was performed by: Shanie Portal
"""


from BayesNet import *
import random
import pandas as pd
import numpy as np

random.seed("aima-python")

T, F = True, False

file = r"titanic.xls"
df = pd.read_excel(file)
print(df)

# survived? and female?

# num female
dfFemale = df.query('sex==\'female\'')
# print(dfFemale.shape[0])
percentFemale = dfFemale.shape[0] / df.shape[0]

# num not female
dfNotFemale = df[df.sex !='female']
print(dfNotFemale.shape[0])
percentNotFemale = dfNotFemale.shape[0] / df.shape[0]


# female
dfSurvivedFemale = df.query('survived==1 and sex==\'female\'')
# print(dfSurvivedFemale)
# P(Survived,Female)/P(Female)
# P(Survived|Female)
percentSurvivedGivenFemale = (dfSurvivedFemale.shape[0]/df.shape[0])/(dfFemale.shape[0]/df.shape[0])

dfSurvivedMale = df.query('survived==1 and sex not in (\'female\')')
print(dfSurvivedMale)
percentSurvivedMale = (dfSurvivedMale.shape[0]/df.shape[0])/(dfNotFemale.shape[0]/df.shape[0])

#### Female
####   |
####   |
####  Survived

TitanicFemaleSurvived = BayesNet([('Female', '', percentFemale),
                                   ('Survived', 'Female',
                      {(T): percentSurvivedGivenFemale, (F): percentSurvivedMale})
                                  ])
print("survived? and Female?")

#Bayes
print ("Given Survived=T", enumeration_ask(
    'Female', dict(Survived=T),
    TitanicFemaleSurvived).show_approx())

print ("Given Female=F", enumeration_ask(
    'Survived', dict(Female=F),
    TitanicFemaleSurvived).show_approx())

print ("Given Female=T", enumeration_ask(
    'Survived', dict(Female=T),
    TitanicFemaleSurvived).show_approx())

########

