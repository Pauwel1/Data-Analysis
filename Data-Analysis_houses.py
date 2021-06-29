### Data-Analysis project ###
### Pauwel De Wilde ###
### BeCode.org - Bouman 3.31 ###

import pandas as pd
import numpy as np
import seaborn as sns

url = "https://raw.githubusercontent.com/jejobueno/challenge-collecting-data/main/assets/housing-data.csv"
df = pd.read_csv(url)


# CLEAN THE DATAFRAME
# sort by location & type
df = df.sort_values(["postalCode"], ascending = False).reset_index()
df = df.iloc[:, 2:]

# rename gardens and terraces as "outsideSpace" and take only the surface value
df.terraceSurface.fillna(0, inplace = True)
df.gardenSurface.fillna(0, inplace = True)
df["outsideSpace"] = df["terraceSurface"] + df["gardenSurface"]

# CUT THE DATAFRAME
# reduntant colums
df = df.drop(["typeSale", "hasFullyEquippedKitchen", "gardenSurface", "terraceSurface", "facadeCount"], axis = 1)

# redundant rows
annuity_index = df[df["subtypeSale"] == "LIFE_ANNUITY"].index
df = df.drop(annuity_index, axis = 0).reset_index()

housegroup_index = df[df["typeProperty"] == "HOUSE_GROUP"].index
df = df.drop(housegroup_index, axis = 0).reset_index()
df = df.iloc[:, 2:]

# print(df.groupby("isFurnished"))
# print(df.groupby("facadeCount").dropna().describe())
# print(df.head(50))
# print(df.tail(50))
# print(df.info())

###############################

# VISUALIZATION
