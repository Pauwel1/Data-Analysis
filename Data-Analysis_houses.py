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


# GET THE DATAFRAME READY
# sort by location & type
df = df.sort_values(["postalCode"], ascending = False).reset_index()
df = df.iloc[:, 2:]

# reorganize gardens and terraces under "outsideSpace"
df.terraceSurface.fillna(0, inplace = True)
df.gardenSurface.fillna(0, inplace = True)
df["outsideSpace"] = df["terraceSurface"] + df["gardenSurface"]

# column per province
df["province"] = df["postalCode"]
df["province"] = df["province"].astype(str).replace(to_replace = r"(1[0-3]\d{2})", value = "BRU", regex = True)	
df["province"] = df["province"].astype(str).replace(to_replace = r"(15\d{2})", value = "VLB", regex = True)	
df["province"] = df["province"].astype(str).replace(to_replace = r"(3[0-4]\d{2})", value = "VLB", regex = True)
df["province"] = df["province"].astype(str).replace(to_replace = r"(1[3-4]\d{2})", value = "WAB", regex = True)
df["province"] = df["province"].astype(str).replace(to_replace = r"(2\d{3})", value = "ANT", regex = True)
df["province"] = df["province"].astype(str).replace(to_replace = r"(35\d{2})", value = "LIM", regex = True)
df["province"] = df["province"].astype(str).replace(to_replace = r"(4\d{3})", value = "LUI", regex = True)
df["province"] = df["province"].astype(str).replace(to_replace = r"(5\d{3})", value = "NAM", regex = True)
df["province"] = df["province"].astype(str).replace(to_replace = r"(6[0-5]\d{2})", value = "HEN", regex = True)
df["province"] = df["province"].astype(str).replace(to_replace = r"(7\d{3})", value = "HEN", regex = True)
df["province"] = df["province"].astype(str).replace(to_replace = r"(6[6-9]\d{2})", value = "LUX", regex = True)
df["province"] = df["province"].astype(str).replace(to_replace = r"(8\d{3})", value = "WVL", regex = True)
df["province"] = df["province"].astype(str).replace(to_replace = r"(9\d{3})", value = "OVL", regex = True)

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

# presentation = df.groupby("province").price.mean()


# df.loc[df.postalCode.astype(str).str.match({r"(1[0-2]\d{2})" : "VB", r"(1[5-9]\d{2})" : "VB", r"(3[0-4]\d{2})" : "VB"})], inplace = True