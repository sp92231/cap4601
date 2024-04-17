"""
Name: Shanie Portal
Date: 04/13/2024
Assignment: Module 12: Project -Learning Decision Tree
Due Date: 04/14/2024
About this project: Measure accuracy on depth/training set size and create a decision tree.
Assumptions:NA
All work below was performed by Shanie Portal and inspired by Dr. Works' videos"""

from sklearn import tree
import pandas as pd
import pydotplus

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

# Change all empty values to the equivalent negative.
# Assumes not a fan if unanswered.
df['starWars_Fan?'] = df['starWars_Fan?'].fillna('No')
# Assumes not familiar if unanswered.
df['expUniverse_Familiar?'] = df['expUniverse_Familiar?'].fillna('No')
# Assumes not a fan if unanswered.
df['starTrek_Fan?'] = df['starTrek_Fan?'].fillna('No')

# Drops rows where columns have NaNs.
# Can't change empty, so remove.
df = df.dropna(axis=0, how='any', subset=['shotFirst?', 'Gender', 'Education'])


# print(df.head())
# print("Name of Columns", df.columns)
# print(df.head(1000))
# print(df.shape[0])  # 512 Overall Rows after trimming

###################################
## 1) Using Sample population.
#Convert categorical variables into indicator variables: 1’s and 0's.
#data = pd.get_dummies(df[ ['sex','pclass','parch'] ])
data = pd.get_dummies(df[['Gender', 'starTrek_Fan?', 'Education',
                          'expUniverse_Familiar?', 'shotFirst?']])

# Print new dummy data.
print(data)

# Decision tree classifier.
clf = tree.DecisionTreeClassifier()

# Split data into test and training set.
x = data
y = df['starWars_Fan?']

# Splits data into train and test sets.
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=.3)
# test_size = .3 means that test set will be 30% of the train set.

# Training the Decision Tree.
clf_train = clf.fit(x_train, y_train)

# Export/Print a decision tree in DOT format.
print(tree.export_graphviz(clf_train, None))

# 2) Graph measuring accuracy based upon TrainingSetSize.
#Accuracy
NumRuns = 5
TrainingSetSize=[]
ScorePer = []
n =0
for per in range(10,55,5):
    TrainingSetSize.append(per*.01)
    ScorePer.append(0)
    for i in range(NumRuns):
        x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=(per*.01),random_state=100)
        # test_size = .1 means that test set will be 10% of the train set.
        # Training the Decision Tree.
        clf_train = clf.fit(x_train, y_train)
        pred = clf_train.predict(x_test)
        ScorePer[n] += accuracy_score(y_test, pred)
        #print(ScorePer[n])
    ScorePer[n] /=NumRuns
    #print(ScorePer[n])
    n+=1

# Plot graph.
d = pd.DataFrame({
 'accuracy':pd.Series(ScorePer),
 'training set size':pd.Series(TrainingSetSize)})

plt.plot('training set size','accuracy', data=d, label='accuracy')
plt.ylabel('accuracy')
plt.xlabel('training set size')
plt.show()