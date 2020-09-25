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
flight = pd.read_csv(win_path)

print(flight.columns)

print(flight.info())

# EDA

# function to print 
def autolabel(rects):
    for i, p in enumerate(rects.patches):
        height = p.get_height()
        rects.text(p.get_x()+p.get_width()/2., height + 0.2,\
            flight["CANCELLED"].value_counts()[i], ha = "center")


# VARIABLE: CANCELLED
flight["CANCELLED"].value_counts()

# Barplot with labels on top
ax = sns.countplot(data = flight, x = "CANCELLED")
autolabel(ax)

flight.isnull().sum()


def missing_value_table(df):
    mis_val = df.isnull().sum()
    mis_val_pct = df.isnull().sum() * 100 / len(df)
    
    # concatenate two columns
    mis_val_tbl = pd.concat([mis_val, mis_val_pct], axis = 1)
    
    # Rename columns 
    mis_val_tbl = mis_val_tbl.rename(columns = {"0":"num NAs", "1", ""})
    
    print(mis_val_tbl)
    
    

# VARIABLE: YEAR
flight["YEAR"].value_counts()
