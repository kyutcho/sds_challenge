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
ax = sns.countplot(data = flight, x = "CANCELLED")

# Barplot with labels on top
autolabel(ax)


# VARIABLE: YEAR
flight["YEAR"].value_counts()

