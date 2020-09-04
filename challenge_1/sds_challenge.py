# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 13:38:27 2020

@author: david
"""

import numpy as np
import pandas as pd

# file_path = "\challenge_1" 
win_path = "D:/Learning/Projects/sds_challenges/challenge_1/data/public_flights.csv"
mac_path = "~/Projects/sds_challenge/challenge_1/data/public_flights.csv"
df = pd.read_csv("~/Projects/sds_challenge/challenge_1/data/public_flights.csv")

print(df.columns)

a = np.array([12,3,5])