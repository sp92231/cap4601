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

# Rename columns
df.rename(columns=colNames, inplace=True)

# Change shotFirst? and Education to boolean values
df['shotFirst?'] = df['shotFirst?'].replace("I don't understand this question", None)

eduMap = {
    'High school degree': 'High School or Less',
    'Less than high school degree': 'High School or Less',
    'Bachelor degree': 'College or More',
    'Some college or Associate degree': 'College or More',
    'Graduate degree': 'College or More'
}

df['Education'] = df['Education'].map(eduMap)

# Change all empty values to the equivalent negative (ie, you can't be a fan if you haven't seen it)
df['starWars_Fan?'] = df['starWars_Fan?'].fillna('No')  # Assuming not a fan if not answered
df['expUniverse_Familiar?'] = df['expUniverse_Familiar?'].fillna('No')  # Assuming not familiar if not answered
df['starTrek_Fan?'] = df['starTrek_Fan?'].fillna('No')  # Assuming not a fan if not answered

# Dropping rows where specified columns have NaNs
df = df.dropna(axis=0, how='any', subset=['shotFirst?', 'Gender', 'Education'])  # Can't change empty to alt, so remove


# print(df.head())
# print("Name of Columns", df.columns)
# print(df.head(1000))
# print(df.shape[0])  # 512 Overall Rows after trimming

###################################
## 1) Using Sample pop
#Now I will convert the categorical variables into dummy/indicator variables or (binary variables) essentially 1’s and 0's.
#data = pd.get_dummies(df[ ['sex','pclass','parch'] ])
data = pd.get_dummies(df[['Gender', 'starTrek_Fan?', 'Education',
                          'expUniverse_Familiar?', 'shotFirst?']])

#print the new dummy data
print(data)

# The decision tree classifier.
clf = tree.DecisionTreeClassifier()

#split data into test and training set
x = data   # Second column until the last column
y = df['starWars_Fan?']


#this function randomly split the data into train and test sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=.45)
#test_size=.3 means that our test set will be 30% of the train set.

# Training the Decision Tree
clf_train = clf.fit(x_train, y_train)
data = pd.get_dummies(df[['Gender', 'starTrek_Fan?', 'Education',
                          'expUniverse_Familiar?', 'shotFirst?']])

#print the new dummy data
#print(data)

#drop any rows with misssing values
data = data.dropna()
#print the new dummy data
#print(data)
x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=.45, random_state=100)

#######################################
# graph measuring accuracy based upon depth of decision tree
max_depth = []
entropy = []
for i in range(1,10):
 dtree = tree.DecisionTreeClassifier(criterion='entropy', max_depth=i)
 dtree.fit(x_train, y_train)
 pred = dtree.predict(x_test)
 entropy.append(accuracy_score(y_test, pred))
 ####
 max_depth.append(i)

#plot graph
d = pd.DataFrame({
 'entropy':pd.Series(entropy),
 'max_depth':pd.Series(max_depth)})

plt.plot('max_depth','entropy', data=d, label='entropy')
plt.xlabel('max_depth')
plt.ylabel('accuracy')
plt.legend()
plt.show()
