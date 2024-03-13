"""

Name: Shanie Portal
Date: 03/03/24
Assignment: Module 7: Project - Uncertainty Python
Due Date: 03/03/24
About this project: This project computes and displays a distribution table from the data set: Star Wars.
Assumptions: Not really assumptions, but chosen columns are:
Have you seen any of the 6 films in the Star Wars franchise? Yes/No
Do you consider yourself to be a fan of the Star Trek film franchise? Yes/No
Gender? Male/Female
All work below was performed by Shanie Portal

"""
import pandas as pd
from prettytable import PrettyTable

# Loading the Star Wars data set.
file = r"StarWars.xlsx"
df = pd.read_excel(file)

# Dropping rows where there are NaNs in the data.
df = df.dropna(axis=0, how='any', subset=['Gender', 'Do you consider yourself to be a fan of the Star Trek franchise?', 'Have you seen any of the 6 films in the Star Wars franchise?'])

# Get Counts
# Male: Trek Y, War Y
dfMaleTrekYWarY = df.query("`Gender` == 'Male' and "
                           "`Do you consider yourself to be a fan of the Star Trek franchise?` == 'Yes' and "
                           "`Have you seen any of the 6 films in the Star Wars franchise?` == 'Yes'")

dfMaleTrekYWarN = df.query("`Gender` == 'Male' and "
                           "`Do you consider yourself to be a fan of the Star Trek franchise?` == 'Yes' and "
                           "`Have you seen any of the 6 films in the Star Wars franchise?` == 'No'")

# Male: Trek N, War Y
dfMaleTrekNWarY = df.query("`Gender` == 'Male' and "
                           "`Do you consider yourself to be a fan of the Star Trek franchise?` == 'No' and "
                           "`Have you seen any of the 6 films in the Star Wars franchise?` == 'Yes'")

# Male: Trek N, War N
dfMaleTrekNWarN = df.query("`Gender` == 'Male' and "
                           "`Do you consider yourself to be a fan of the Star Trek franchise?` == 'No' and "
                           "`Have you seen any of the 6 films in the Star Wars franchise?` == 'No'")

# Female: Trek Y, War Y
dfFemaleTrekYWarY = df.query("`Gender` == 'Female' and "
                             "`Do you consider yourself to be a fan of the Star Trek franchise?` == 'Yes' and "
                             "`Have you seen any of the 6 films in the Star Wars franchise?` == 'Yes'")
# Female: Trek Y, War N
dfFemaleTrekYWarN = df.query("`Gender` == 'Female' and "
                             "`Do you consider yourself to be a fan of the Star Trek franchise?` == 'Yes' and "
                             "`Have you seen any of the 6 films in the Star Wars franchise?` == 'No'")
# Female: Trek N, War Y
dfFemaleTrekNWarY = df.query("`Gender` == 'Female' and "
                             "`Do you consider yourself to be a fan of the Star Trek franchise?` == 'No' and "
                             "`Have you seen any of the 6 films in the Star Wars franchise?` == 'Yes'")

dfFemaleTrekNWarN = df.query("`Gender` == 'Female' and "
                             "`Do you consider yourself to be a fan of the Star Trek franchise?` == 'No'  and "
                             "`Have you seen any of the 6 films in the Star Wars franchise?` == 'No'")

# Count Gender totals.
dfMale = df.query("`Gender` == 'Male'")
dfFemale = df.query("`Gender` == 'Female'")

# Count Fan totals.
dfNotTrek = df.query("`Do you consider yourself to be a fan of the Star Trek franchise?` == 'No'")
dfFanTrek = df.query("`Do you consider yourself to be a fan of the Star Trek franchise?` == 'Yes'")

# Count for Seen Star Wars totals.
dfNotStar = df.query("`Have you seen any of the 6 films in the Star Wars franchise?` == 'No'")
dfSeenStar = df.query("`Have you seen any of the 6 films in the Star Wars franchise?` == 'Yes'")

# Table for counts.
x = PrettyTable(['Gender', 'Fan of Star Trek and Seen Star Wars', 'Fan of Star Trek and Not Watched Star Wars',
                 'Not a Fan of Star Trek and Seen Star Wars', 'Not A Fan nor Seen Star Wars'])
x.add_row(['Female', dfFemaleTrekYWarY.shape[0], dfFemaleTrekYWarN.shape[0],
           dfFemaleTrekNWarY.shape[0], dfFemaleTrekNWarN.shape[0]])
x.add_row(['Male', dfMaleTrekYWarY.shape[0], dfMaleTrekYWarN.shape[0],
           dfMaleTrekNWarY.shape[0], dfMaleTrekNWarN.shape[0]])
x.add_row(["-----", "-----", "-----", "-----", "-----"])
x.add_row(['Total', dfFemaleTrekYWarY.shape[0] + dfMaleTrekYWarY.shape[0],
           dfFemaleTrekYWarN.shape[0] + dfMaleTrekYWarN.shape[0],
           dfFemaleTrekNWarY.shape[0] + dfMaleTrekNWarY.shape[0],
           dfFemaleTrekNWarN.shape[0] + dfMaleTrekNWarN.shape[0]])

total = (dfFemaleTrekYWarY.shape[0] + dfMaleTrekYWarY.shape[0] + dfFemaleTrekYWarN.shape[0]
         + dfMaleTrekYWarN.shape[0] + dfFemaleTrekNWarY.shape[0] + dfMaleTrekNWarY.shape[0]
         + dfFemaleTrekNWarN.shape[0] + dfMaleTrekNWarN.shape[0])
print("Totals: ", total, str(df.shape[0]), "\n")

print(x.get_string(title="Star Wars Preferences - (Count)"))
print("\n")

# Create Joint Distribution Table
tableJoint = PrettyTable(['Gender', 'Fan of Star Trek and Seen Star Wars', 'Fan of Star Trek and Not Watched Star Wars',
                          'Not a Fan of Star Trek and Seen Star Wars', 'Not A Fan nor Seen Star Wars'])
tableJoint.add_row(['Female', round(dfFemaleTrekYWarY.shape[0] / total * 100.0, 2),
                    round(dfFemaleTrekYWarN.shape[0] / total * 100.0, 2),
                    round(dfFemaleTrekNWarY.shape[0] / total * 100.0, 2),
                    round(dfFemaleTrekNWarN.shape[0] / total * 100.0, 2)])
tableJoint.add_row(['Male', round(dfMaleTrekYWarY.shape[0] / total * 100.0, 2),
                    round(dfMaleTrekYWarN.shape[0] / total * 100.0, 2),
                    round(dfMaleTrekNWarY.shape[0] / total * 100.0, 2),
                    round(dfMaleTrekNWarN.shape[0] / total * 100.0, 2)])
tableJoint.add_row(["-----", "-----", "-----", "-----", "-----"])
tableJoint.add_row(['Total', round((dfFemaleTrekYWarY.shape[0] + dfMaleTrekYWarY.shape[0]) / total * 100.0, 2),
                    round((dfFemaleTrekYWarN.shape[0] + dfMaleTrekYWarN.shape[0]) / total * 100.0, 2),
                    round((dfFemaleTrekNWarY.shape[0] + dfMaleTrekNWarY.shape[0]) / total * 100.0, 2),
                    round((dfFemaleTrekNWarN.shape[0] + dfMaleTrekNWarN.shape[0]) / total * 100.0, 2)])

print(tableJoint.get_string(title="Star Wars Preferences - (Percentages)"))
print("\n")

print("Probability Chances: Gender")
print("      Female: " + str(round(dfFemale.shape[0] / total * 100.0, 2)))
print("        Male: " + str(round(dfMale.shape[0] / total * 100.0, 2)))

print("Probability Chances: Fan of Star Trek")
print("         Fan: " + str(round(dfFanTrek.shape[0] / total * 100.0, 2)))
print("   Not a Fan: " + str(round(dfNotTrek.shape[0] / total * 100.0, 2)))

print("Probability Chances: Seen Star Wars")
print("         Fan: " + str(round(dfSeenStar.shape[0] / total * 100.0, 2)))
print("   Not a Fan: " + str(round(dfNotStar.shape[0] / total * 100.0, 2)))
print("\n")

# P(A1 v A2) = P(A1) + P(A2) - P(A1 and A2)
pFemale = dfFemale.shape[0]
pMale = dfMale.shape[0]
pFanTrek = dfFanTrek.shape[0]
pNotTrek = dfNotTrek.shape[0]

# Female, Fan of Star Trek
dfFemTrek = df.query("`Gender` == 'Female' and "
                     "`Do you consider yourself to be a fan of the Star Trek franchise?` == 'Yes'")
pFemTrek = dfFemTrek.shape[0]
print("p(female v fan of star trek)=", round((pFemale + pFanTrek - pFemTrek) / total * 100, 3), "%")
# Female, Not fan of Star Trek
dfFemTrekN = df.query("`Gender` == 'Female' and "
                      "`Do you consider yourself to be a fan of the Star Trek franchise?` == 'No'")
pFemTrekN = dfFemTrekN.shape[0]
print("p(female v not fan of star trek)=", round((pFemale + pNotTrek - pFemTrekN) / total * 100, 3), "%")

# Male, Fan of Star Trek
dfMaleTrek = df.query("`Gender` == 'Male' and "
                      "`Do you consider yourself to be a fan of the Star Trek franchise?` == 'Yes'")
pMaleTrek = dfMaleTrek.shape[0]
print("p(male v fan of star trek)=", round((pMale + pFanTrek - pMaleTrek) / total * 100, 3), "%")
# Male, Not fan of Star Trek
dfMaleTrekN = df.query("`Gender` == 'Male' and "
                       "`Do you consider yourself to be a fan of the Star Trek franchise?` == 'No'")
pMaleTrekN = dfMaleTrekN.shape[0]
print("p(male v not fan of star trek)=", round((pMale + pNotTrek - pMaleTrekN) / total * 100, 3), "%")
print("")

# P(A1, A3), A1 = Gender A3 = Star Wars
# Female, Watched Star Wars
dfFemStar = df.query("`Gender` == 'Female' and "
                     "`Have you seen any of the 6 films in the Star Wars franchise?` == 'Yes'")
pFemStar = dfFemStar.shape[0]
print("p(female, watched star wars) =", round(pFemStar / total * 100, 3), "%")

# Female, Not Watched Star Wars
dfFemNStar = df.query("`Gender` == 'Female' and "
                      "`Have you seen any of the 6 films in the Star Wars franchise?` == 'No'")
pFemNStar = dfFemNStar.shape[0]

# Male, Watched Star Wars
print("p(female, not watched star wars) =", round(pFemNStar / total * 100, 3), "%")
dfMaleStar = df.query("`Gender` == 'Male' and "
                      "`Have you seen any of the 6 films in the Star Wars franchise?` == 'Yes'")

pMaleStar = dfMaleStar.shape[0]
print("p(male, watched star wars) =", round(pMaleStar / total * 100, 3), "%")

# Male, Not Watched Star Wars
dfMaleNStar = df.query("`Gender` == 'Male' and "
                       "`Have you seen any of the 6 films in the Star Wars franchise?` == 'No'")
pMaleNStar = dfMaleNStar.shape[0]
print("p(male, not watched star wars) =", round(pMaleNStar / total * 100, 3), "%")
print("\n")

# P(A2 | A1, A3)
# Female | Watched Star Wars, Fan of Star Trek
pFemStarTrekY = dfFemaleTrekYWarY.shape[0] / pFemStar
print("p(fan of star trek | female, watched star wars) =", round(pFemStarTrekY * 100, 3), "%")

# Female, Watched Star Wars, Not Fan of Star Trek
pFemStarTrekN = dfFemaleTrekNWarY.shape[0] / pFemStar
print("p(not fan of star trek | female, watched star wars) =", round(pFemStarTrekN * 100, 3), "%")

# Female, Not Watched Star Wars, Fan of Star Trek
pFemNStarTrekY = dfFemaleTrekYWarN.shape[0] / pFemNStar
print("p(fan of star trek | female, not watched star wars) =", round(pFemNStarTrekY * 100, 3), "%")

# Female, Not Watched Star Wars, Not Fan of Star Trek
pFemNStarTrekN = dfFemaleTrekNWarN.shape[0] / pFemNStar
print("p(not fan of star trek | female, not watched star wars) =", round(pFemNStarTrekN * 100, 3), "%")

# Male, Watched Star Wars, Fan of Star Trek
pMaleStarTrekY = dfMaleTrekYWarY.shape[0] / pMaleStar
print("p(fan of star trek | male, watched star wars) =", round(pMaleStarTrekY * 100, 3), "%")

# Male, Watched Star Wars, Not Fan of Star Trek
pMaleStarTrekN = dfMaleTrekNWarY.shape[0] / pMaleStar
print("p(not fan of star trek | male, watched star wars) =", round(pMaleStarTrekN * 100, 3), "%")

# Male, Not Watched Star Wars, Fan of Star Trek
pMaleNStarTrekY = dfMaleTrekYWarN.shape[0] / pMaleNStar
print("p(fan of star trek | male, not watched star wars) =", round(pMaleNStarTrekY * 100, 3), "%")

# Male, Not Watched Star Wars, Not Fan of Star Trek
pMaleNStarTrekN = dfMaleTrekNWarN.shape[0] / pMaleNStar
print("p(not fan of star trek | male, not watched star wars) =", round(pMaleNStarTrekN * 100, 3), "%")
print("\n")

# using Bayes P( A1, A3| A2)
# Female, Watched Star Wars | Fan Trek
pFemStarGivenFanTrek = (pFemStarTrekY * pFanTrek) / total
print("p(female, watched star wars | fan trek) =", round(pFemStarGivenFanTrek * 100, 3), "%")
# Female, Watched Star Wars | Not Fan Trek
pFemStarGivenNotFanTrek = (pFemStarTrekN * pNotTrek) / total
print("p(female, watched star wars | not fan trek) =", round(pFemStarGivenNotFanTrek * 100, 3), "%")
# Female, Not Watched Star Wars | Fan Trek
pFemNStarGivenFanTrek = (pFemNStarTrekY * pFanTrek) / total
print("p(female, not watched star wars | fan trek) =", round(pFemNStarGivenFanTrek * 100, 3), "%")
# Female, Not Watched Star Wars | Not Fan Trek
pFemNStarGivenNotFanTrek = (pFemNStarTrekN * pNotTrek) / total
print("p(female, not watched star wars | not fan trek) =", round(pFemNStarGivenNotFanTrek * 100, 3), "%")

# Male, Watched Star Wars | Fan Trek
pMaleStarGivenFanTrek = (pMaleStarTrekY * pFanTrek) / total
print("p(male, watched star wars | fan trek) =", round(pMaleStarGivenFanTrek * 100, 3), "%")
# Male, Watched Star Wars | Not Fan Trek
pMaleStarGivenNotFanTrek = (pMaleStarTrekN * pNotTrek) / total
print("p(male, watched star wars | not fan trek) =", round(pMaleStarGivenNotFanTrek * 100, 3), "%")
# Male, Not Watched Star Wars | Fan Trek
pMaleNStarGivenFanTrek = (pMaleNStarTrekY * pFanTrek) / total
print("p(male, not watched star wars | fan trek) =", round(pMaleNStarGivenFanTrek * 100, 3), "%")
# Male, Not Watched Star Wars | Not Fan Trek
pMaleNStarGivenNotFanTrek = (pMaleNStarTrekN * pNotTrek) / total
print("p(male, not watched star wars | not fan trek) =", round(pMaleNStarGivenNotFanTrek * 100, 3), "%")


