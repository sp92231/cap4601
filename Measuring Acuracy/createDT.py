"""
Name: Shanie Portal
Date: 04/13/2024
Assignment: Module 12: Project -Learning Decision Tree
Due Date: 04/14/2024
About this project: Measure accuracy on depth/training set size and create a decision tree.
Assumptions:NA
All work below was performed by Shanie Portal and inspired by Dr. Works's videos.
"""

## Use Python 3.10

from sklearn import tree  # For our Decision Tree
import pandas as pd  # For our DataFrame
import pydotplus  # To create our Decision Tree Graph

from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

import matplotlib.pyplot as plt
from sklearn.utils import graph

file = r"StarWars.xlsx"
df = pd.read_excel(file)

# Dictionary.
colNames = {
    'Education': 'Education',
    'Do you consider yourself to be a fan of the Star Wars film franchise?': 'starWars_Fan?',
    'Which character shot first?': 'shotFirst?',
    'Are you familiar with the Expanded Universe?': 'expUniverse_Familiar?',
    'Do you consider yourself to be a fan of the Star Trek franchise?': 'starTrek_Fan?',
    'Gender': 'Gender'
}

# Rename columns.
df.rename(columns=colNames, inplace=True)

# Change to boolean values.
df['shotFirst?'] = df['shotFirst?'].replace("I don't understand this question", None)

eduMap = {
    'High school degree': 'High School or Less',
    'Less than high school degree': 'High School or Less',
    'Bachelor degree': 'College or More',
    'Some college or Associate degree': 'College or More',
    'Graduate degree': 'College or More'
}

df['Education'] = df['Education'].map(eduMap)

# Change empty values to the equivalent negative.
# Assumes not a fan if unanswered.
df['starWars_Fan?'] = df['starWars_Fan?'].fillna('No')
# Assumes not familiar if unanswered.
df['expUniverse_Familiar?'] = df['expUniverse_Familiar?'].fillna('No')
# Assumes not a fan if unanswered.
df['starTrek_Fan?'] = df['starTrek_Fan?'].fillna('No')

# Drops rows where columns have NaNs.
df = df.dropna(axis=0, how='any', subset=['shotFirst?', 'Gender', 'Education'])  # Can't change empty to alt, so remove

# print(df.head())
# print("Name of Columns", df.columns)
# print(df.head(1000))
# 512 Overall Rows after trimming.
# print(df.shape[0])

###################################

# 1) Using Sample population.
# Converts the categorical variables into indicator variables: 1s / 0s.
data = pd.get_dummies(df[['Education', 'Gender', 'shotFirst?', 'starTrek_Fan?']])

# Prints the new dummy data.
print(data)

# Split data into test and training set.
x = data
y = df['starWars_Fan?']

# Splits the data into train and test sets.
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=.3)
# test_size = .3 means that test set will be 30% of the train set.

# Training the Decision Tree.
clf = tree.DecisionTreeClassifier(criterion='entropy')
clf_train = clf.fit(x_train, y_train)

# Print a decision tree in DOT format.
print(tree.export_graphviz(clf_train, None))

# Create Dot Data.
dot_data = tree.export_graphviz(clf_train, out_file=None, feature_names=list(data.columns.values),
                                class_names=['Not Fan', 'Fan'], rounded=True,
                                filled=True)
# Create Graph from DOT data.
graph = pydotplus.graph_from_dot_data(dot_data)

# Create PDF.
graph.write_pdf("DecisionTree.pdf")
