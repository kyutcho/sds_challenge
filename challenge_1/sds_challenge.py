# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 13:38:27 2020

@author: Jayden Cho - sds_challenge
"""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# file_path = "\challenge_1"
win_path = "D:/Learning/Projects/sds_challenges/challenge_1/data/public_flights.csv"
mac_path = "~/Projects/sds_challenge/challenge_1/data/public_flights.csv"
df = pd.read_csv(win_path)

print(df.columns)

print(df.info())

# sns.distplot(df['DISTANCE']);

# EDA

# Cancelled
df["CANCELLED"].value_counts()[0]
g = sns.countplot(data = df, x = "CANCELLED")
print(type(g))

plt.annotate(str(df["CANCELLED"].value_counts()[0]), )

sns.catplot(data = df, x = "YEAR", kind = "count")
df["YEAR"].value_counts()

