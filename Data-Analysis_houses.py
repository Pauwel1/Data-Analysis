### Data-Analysis project ###
### Pauwel De Wilde ###
### BeCode.org - Bouman 3.31 ###

import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import re

url = "https://raw.githubusercontent.com/jejobueno/challenge-collecting-data/main/assets/housing-data.csv"
df = pd.read_csv(url)


# CLEAN THE DATAFRAME
# sort by location & type
df = df.sort_values(["postalCode"], ascending = False).reset_index()
df = df.iloc[:, 2:]

# reorganize gardens and terraces under "outsideSpace"
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

df.drop_duplicates(['postalCode','price'],keep= 'last')

# print(df.groupby("isFurnished"))
# print(df.groupby("facadeCount").dropna().describe())
# print(df.head(50))
# print(df.tail(50))
# print(df.info())

###############################

# CREATE SEPERATE DATAFRAMES
# per region
df_zone1000 = df.loc[df.postalCode.astype(str).str.match(r"(1\d{3})")]
df_zone2000 = df.loc[df.postalCode.astype(str).str.match(r"(2\d{3})")]
df_zone3000 = df.loc[df.postalCode.astype(str).str.match(r"(3\d{3})")]
df_zone4000 = df.loc[df.postalCode.astype(str).str.match(r"(4\d{3})")]
df_zone5000 = df.loc[df.postalCode.astype(str).str.match(r"(5\d{3})")]
df_zone6000 = df.loc[df.postalCode.astype(str).str.match(r"(6\d{3})")]
df_zone7000 = df.loc[df.postalCode.astype(str).str.match(r"(7\d{3})")]
df_zone8000 = df.loc[df.postalCode.astype(str).str.match(r"(8\d{3})")]
df_zone9000 = df.loc[df.postalCode.astype(str).str.match(r"(9\d{3})")]

print(df_zone1000.head(50))

# per property type
df_houses = df[df["typeProperty"] == "HOUSE"]
df_apartments = df[df["typeProperty"] == "Apartment"]

###############################

# VISUALIZATION

# sns.lmplot(x = "price", y = "postalCode", data = df_houses, hue = "subtypeProperty")
# plt.xlim(0, None)
# plt.ylim(0, 10000)
# plt.show()

# sns.boxplot(data = df_houses, x = "postalCode", y = "price", hue = "subtypeProperty")
# plt.show()