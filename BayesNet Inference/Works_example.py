#pip install -r requirements.txt
#pip install ipythonblocks
#pip install pandas
#pip install xlrd

import pytest

from probability4e import *
from utils import rounder
import pandas as pd
import numpy as np

random.seed("aima-python")

T, F = True, False

file = r"D:\data-master\titanic\titanic.xls"
df = pd.read_excel(file)
print(df)

# survived? and female?

# num female
dfFemale = df.query('sex==\'female\'')
# print(dfFemale.shape[0])
percentFemale = dfFemale.shape[0] / df.shape[0]


# female
dfSurvivedFemale = df.query('survived==1 and sex==\'female\'')
# print(dfSurvivedFemale)
percentSurvivedGivenFemale = (dfSurvivedFemale.shape[0]/df.shape[0])/(dfFemale.shape[0]/df.shape[0])

dfDiedFemale = df.query('survived==0 and sex==\'female\'')
# print(dfDiedFemale)
percentDiedGivenFemale = (dfDiedFemale.shape[0]/df.shape[0])/(dfFemale.shape[0]/df.shape[0])


TitanicFemaleSurvived = BayesNet(
    [('Female', '', percentFemale),
     ('Survived', 'Female',
    {(T): percentSurvivedGivenFemale, (F): percentDiedGivenFemale})
        ])
print("survived? and Female?")

#Bayes
print (enumeration_ask(
    'Female', dict(Survived=T),
    TitanicFemaleSurvived).show_approx())

print (elimination_ask(
    'Female', dict(Survived=F),
    TitanicFemaleSurvived).show_approx())


print (enumeration_ask(
    'Survived', dict(Female=T),
    TitanicFemaleSurvived).show_approx())

print (elimination_ask(
    'Survived', dict(Female=F),
    TitanicFemaleSurvived).show_approx())

########

P = JointProbDist(['Female', 'FirstClass'])
dfTest = df.query('sex==\'male\' and pclass>1')
P[0, 0] = dfTest.shape[0]/df.shape[0]

dfTest = df.query('sex==\'male\' and pclass==1')
P[0, 1] = dfTest.shape[0]/df.shape[0]

dfTest = df.query('sex==\'female\' and pclass==1')
P[1, 1] = dfTest.shape[0]/df.shape[0]

dfTest = df.query('sex==\'female\' and pclass>1')
P[1, 0] = dfTest.shape[0]/df.shape[0]
print(P.variables)
print(P.prob)
print(is_independent(['Female', 'FirstClass'], P))
