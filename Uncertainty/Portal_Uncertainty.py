"""

Name: Shanie Portal
Date: 03/03/24
Assignment: Module 7: Project - Uncertainty Python
Due Date: 03/03/24
About this project: This project computes and displays a distribution table from the data set: steak-risk-survey.
Assumptions: Not exactly an assumption, but it should be noted that there are rows in the excel file that do not
answer for the question of Gender when they do not eat steak, but some of them do answer for Gender when they do not eat
steak. This gives a total percentage of under 100%, but I have verified that the correct totals are being counted
when compared to the values received from analyzing in excel.
All work below was performed by Shanie Portal

"""
import pandas as pd
import numpy as np
from prettytable import PrettyTable

# Loading the steak-risk-survey data set.
file = r"steak-risk-survey.xlsx"
df = pd.read_excel(file)

# Females who do not eat steak.
dfFemaleNoSteak = df.query("Gender == 'Female' and `Do you eat steak?` == 'No'")

# Females who eat their steak Rare.
dfFemaleRare = df.query("Gender == 'Female' and `How do you like your steak prepared?` == 'Rare'")

# Females who eat their steak Medium rare.
dfFemaleMediumRare = df.query("Gender == 'Female' and `How do you like your steak prepared?` == 'Medium rare'")

# Females who eat their steak Medium.
dfFemaleMedium = df.query("Gender == 'Female' and `How do you like your steak prepared?` == 'Medium'")

# Females who eat their steak Medium Well.
dfFemaleMediumWell = df.query("Gender == 'Female' and `How do you like your steak prepared?` == 'Medium Well'")

# Females who eat their steak Well.
dfFemaleWell = df.query("Gender == 'Female' and `How do you like your steak prepared?` == 'Well'")

# Males who do not eat steak.
dfMaleNoSteak = df.query("Gender == 'Male' and `Do you eat steak?` == 'No'")

# Males who eat their steak Rare.
dfMaleRare = df.query("Gender == 'Male' and `How do you like your steak prepared?` == 'Rare'")

# Males who eat their steak Medium rare.
dfMaleMediumRare = df.query("Gender == 'Male' and `How do you like your steak prepared?` == 'Medium rare'")

# Male who eat their steak Medium.
dfMaleMedium = df.query("Gender == 'Male' and `How do you like your steak prepared?` == 'Medium'")

# Male who eat their steak Medium Well.
dfMaleMediumWell = df.query("Gender == 'Male' and `How do you like your steak prepared?` == 'Medium Well'")

# Male who eat their steak Well.
dfMaleWell = df.query("Gender == 'Male' and `How do you like your steak prepared?` == 'Well'")

# Steak preference count table.
x = PrettyTable()
x.field_names = ["", "Female", "Male"]
x.add_row(["No Steak", dfFemaleNoSteak.shape[0], dfMaleNoSteak.shape[0]])
x.add_row(["Rare", dfFemaleRare.shape[0], dfMaleRare.shape[0]])
x.add_row(["Medium rare", dfFemaleMediumRare.shape[0], dfMaleMediumRare.shape[0]])
x.add_row(["Medium", dfFemaleMedium.shape[0], dfMaleMedium.shape[0]])
x.add_row(["Medium Well", dfFemaleMediumWell.shape[0], dfMaleMediumWell.shape[0]])
x.add_row(["Well", dfFemaleWell.shape[0], dfMaleWell.shape[0]])
x.add_row(["------","------","------"])
x.add_row(["Total", dfFemaleNoSteak.shape[0] + dfFemaleRare.shape[0] + dfFemaleMediumRare.shape[0] + dfFemaleMedium.shape[0]
              + dfFemaleMediumWell.shape[0] + dfFemaleWell.shape[0], dfMaleNoSteak.shape[0] + dfMaleRare.shape[0] + dfMaleMediumRare.shape[0] +
          dfMaleMedium.shape[0] + dfMaleMediumWell.shape[0] + dfMaleWell.shape[0]])
# Print table.
print(x.get_string(title="Steak Preference (count)"))

# Steak preference percentage table.
y = PrettyTable()
y.field_names = ["", "Female", "Male"]
y.add_row(["No Steak", round(dfFemaleNoSteak.shape[0]/df.shape[0]*100.0,2), round(dfMaleNoSteak.shape[0]/df.shape[0]*100.0,2)])
y.add_row(["Rare", round(dfFemaleRare.shape[0]/df.shape[0]*100.0,2), round(dfMaleRare.shape[0]/df.shape[0]*100.0,2)])
y.add_row(["Medium rare", round(dfFemaleMediumRare.shape[0]/df.shape[0]*100.0,2), round(dfMaleMediumRare.shape[0]/df.shape[0]*100.0,2)])
y.add_row(["Medium", round(dfFemaleMedium.shape[0]/df.shape[0]*100.0,2), round(dfMaleMedium.shape[0]/df.shape[0]*100.0,2)])
y.add_row(["Medium Well", round(dfFemaleMediumWell.shape[0]/df.shape[0]*100.0,2), round(dfMaleMediumWell.shape[0]/df.shape[0]*100.0,2)])
y.add_row(["Well", round(dfFemaleWell.shape[0]/df.shape[0]*100.0,2), round(dfMaleWell.shape[0]/df.shape[0]*100.0,2)])
y.add_row(["------","------","------"])
y.add_row(["Total", round((dfFemaleNoSteak.shape[0] + dfFemaleRare.shape[0] + dfFemaleMediumRare.shape[0] + dfFemaleMedium.shape[0]
              + dfFemaleMediumWell.shape[0] + dfFemaleWell.shape[0])/df.shape[0]*100.0,2), round((dfMaleNoSteak.shape[0] + dfMaleRare.shape[0] + dfMaleMediumRare.shape[0] +
          dfMaleMedium.shape[0] + dfMaleMediumWell.shape[0] + dfMaleWell.shape[0])/df.shape[0]*100.0,2)])
# Print table.
print(y.get_string(title="Steak Preference (percentage)"))

# Compute and display P(A1), P(A2), P(A3).
# Calculate probability of A1: Gender.
print("Probability of A1: Gender:")
# Probability of Female.
dfFemale = df.query("Gender == 'Female'")
pFemale = round((dfFemale.shape[0]/df.shape[0])*100,2)
print("Probability of Gender being Female: ", pFemale,"%")

# Probability of Male.
dfMale = df.query("Gender == 'Male'")
pMale = round((dfMale.shape[0]/df.shape[0])*100,2)
print("Probability of Gender being Male: ", pMale,"%\n")

# Calculate probability of A2: "Do you eat steak?"
print("Probability of A2: Do you eat steak?:")
# Probability of NOT eating steak.
dfNoSteak = df.query("`Do you eat steak?` == 'No'")
pNoSteak = round((dfNoSteak.shape[0]/df.shape[0])*100,2)
print("Probability of NOT eating steak ", pNoSteak,"%")

# Probability of eating steak.
dfYesSteak = df.query("`Do you eat steak?` == 'Yes'")
pYesSteak = round((dfYesSteak.shape[0]/df.shape[0])*100,2)
print("Probability of eating steak ", pYesSteak,"%\n")

# Calculate probability of A3: "How do you like your steak prepared?"
print("Probability of A3: How do you like your steak prepared?:")
# Probability of Rare.
dfRare = df.query("`How do you like your steak prepared?` == 'Rare'")
pRare = round((dfRare.shape[0]/df.shape[0])*100,2)
print("Probability of preferring Rare ", pRare,"%")

# Probability of Medium rare.
dfMediumRare = df.query("`How do you like your steak prepared?` == 'Medium rare'")
pMediumRare = round((dfMediumRare.shape[0]/df.shape[0])*100,2)
print("Probability of preferring Medium rare ", pMediumRare,"%")

# Probability of Medium.
dfMedium = df.query("`How do you like your steak prepared?` == 'Medium'")
pMedium = round((dfMedium.shape[0]/df.shape[0])*100,2)
print("Probability of preferring Medium ", pMedium,"%")

# Probability of Medium Well.
dfMediumWell = df.query("`How do you like your steak prepared?` == 'Medium Well'")
pMediumWell = round((dfMediumWell.shape[0]/df.shape[0])*100,2)
print("Probability of preferring Medium Well ", pMediumWell,"%")

# Probability of Well.
dfWell = df.query("`How do you like your steak prepared?` == 'Well'")
pWell = round((dfWell.shape[0]/df.shape[0])*100,2)
print("Probability of preferring Well ", pWell,"%\n")

# Compute and display P(A1 v A2) and P(A1, A3).
# Calculate probability of gender OR "Do you eat steak?":
print("Probability of gender OR `Do you eat steak?` (P(A1 v A2))")
# Females OR do NOT eat steak:
pFemaleNoSteak = round((dfFemaleNoSteak.shape[0]/df.shape[0])*100,2)
print("Probability of female OR does NOT eat steak: ", round(pFemale + pNoSteak - pFemaleNoSteak), "%")
# Females OR does eat steak:
dfFemaleYesSteak = df.query("Gender == 'Female' and `Do you eat steak?` == 'Yes'")
pFemaleYesSteak = round((dfFemaleYesSteak.shape[0]/df.shape[0])*100,2)
print("Probability of female OR does eat steak: ", round(pFemale + pYesSteak - pFemaleYesSteak), "%")

# Males OR do NOT eat steak:
pMaleNoSteak = round((dfMaleNoSteak.shape[0]/df.shape[0])*100,2)
print("Probability of Male OR does NOT eat steak: ", round(pMale + pNoSteak - pMaleNoSteak), "%")
# Males OR does eat steak:
dfMaleYesSteak = df.query("Gender == 'Male' and `Do you eat steak?` == 'Yes'")
pMaleYesSteak = round((dfMaleYesSteak.shape[0]/df.shape[0])*100,2)
print("Probability of Male OR does eat steak: ", round(pMale + pYesSteak - pMaleYesSteak), "%\n")

# Calculate probability of gender AND "How do you like your steak prepared?"
print("Probability of gender AND `How do you like your steak prepared?` (P(A1, A3))")
# Calculate probability of female AND Rare.
pFemaleRare = round((dfFemaleRare.shape[0]/df.shape[0])*100,2)
print("Probability of Female AND Rare: ", round(pFemale + pRare - pFemaleRare), "%")

# Calculate probability of female AND Medium rare.
pFemaleMediumRare = round((dfFemaleMediumRare.shape[0]/df.shape[0])*100,2)
print("Probability of Female AND Medium rare: ", round(pFemale + pMediumRare - pFemaleMediumRare), "%")

# Calculate probability of female AND Medium.
pFemaleMedium = round((dfFemaleMedium.shape[0]/df.shape[0])*100,2)
print("Probability of Female AND Medium: ", round(pFemale + pMedium - pFemaleMedium), "%")

# Calculate probability of female AND Medium Well.
pFemaleMediumWell = round((dfFemaleMediumWell.shape[0]/df.shape[0])*100,2)
print("Probability of Female AND Medium Well: ", round(pFemale + pMediumWell - pFemaleMediumWell), "%")

# Calculate probability of female AND Well.
pFemaleWell = round((dfFemaleWell.shape[0]/df.shape[0])*100,2)
print("Probability of Female AND Well: ", round(pFemale + pWell - pFemaleWell), "%\n")

# Calculate probability of male AND Rare.
pMaleRare = round((dfMaleRare.shape[0]/df.shape[0])*100,2)
print("Probability of Male AND Rare: ", round(pMale + pRare - pMaleRare), "%")

# Calculate probability of male AND Medium rare.
pMaleMediumRare = round((dfMaleMediumRare.shape[0]/df.shape[0])*100,2)
print("Probability of Male AND Medium rare: ", round(pMale + pMediumRare - pMaleMediumRare), "%")

# Calculate probability of male AND Medium.
pMaleMedium = round((dfMaleMedium.shape[0]/df.shape[0])*100,2)
print("Probability of Male AND Medium: ", round(pMale + pMedium - pMaleMedium), "%")

# Calculate probability of male AND Medium Well.
pMaleMediumWell = round((dfMaleMediumWell.shape[0]/df.shape[0])*100,2)
print("Probability of Male AND Medium Well: ", round(pMale + pMediumWell - pMaleMediumWell), "%")

# Calculate probability of male AND Well.
pMaleWell = round((dfMaleWell.shape[0]/df.shape[0])*100,2)
print("Probability of Male AND Well: ", round(pMale + pWell - pMaleWell), "%")

# Compute and display P(A2 | A1, A3).
# Calculate conditional probability of eating steak as a specific gender with specific cook preference:
# Calculate conditional probabiilty of eating steak as a female who prefers rare steak.

# Calculate conditional probabiilty of eating steak as a male who prefers well steak.