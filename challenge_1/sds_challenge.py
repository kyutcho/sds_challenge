# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 13:38:27 2020

@author: Jayden Cho - sds_challenge
"""

import numpy as np
import pandas as pd
import seaborn as sns

# file_path = "\challenge_1"
win_path = "D:/Learning/Projects/sds_challenges/challenge_1/data/public_flights.csv"
mac_path = "~/Projects/sds_challenge/challenge_1/data/public_flights.csv"
df = pd.read_csv(mac_path)

print(df.columns)

print(df.info())

# sns.distplot(df['DISTANCE']);

df['CANCELLED'].value_counts()

a = np.array([12, 3, 5])
b = np.array([3, 4, 5])
