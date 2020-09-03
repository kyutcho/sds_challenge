# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 13:38:27 2020

@author: Jayden Cho - sds_challenge
"""

import numpy as np
import pandas as pd
import seaborn as sns

# file_path = "\challenge_1" 
df = pd.read_csv("..\data\public_flights.csv")

print(df.columns)

print(df.info())

# sns.distplot(df['DISTANCE']);

df['CANCELLED'].value_counts()

a = np.array([12,3,5])

