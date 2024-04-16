"""
Name: Shanie Portal
Date: 04/13/2024
Assignment: Module 12: Project -Learning Decision Tree
Due Date: 04/14/2024
About this project: Measure accuracy on depth/training set size and create a decision tree.
Assumptions:NA
All work below was performed by Shanie Portal and Dr. Works"""

from sklearn import tree #For our Decision Tree
import pandas as pd # For our DataFrame
import pydotplus # To create our Decision Tree Graph

from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

#pip install matplotlib
import matplotlib.pyplot as plt
from sklearn.utils import graph

file = r"StarWars.xlsx"
df = pd.read_excel(file)

# Dictionary to simplify the long column names
colNames = {
    'Education': 'Education',
    'Do you consider yourself to be a fan of the Star Wars film franchise?': 'starWars_Fan?',
    'Which character shot first?': 'shotFirst?',
    'Are you familiar with the Expanded Universe?': 'expUniverse_Familiar?',
    'Do you consider yourself to be a fan of the Star Trek franchise?': 'starTrek_Fan?',
    'Gender': 'Gender'
}

