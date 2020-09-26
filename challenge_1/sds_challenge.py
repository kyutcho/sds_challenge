# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 13:38:27 2020

@author: Jayden Cho - sds_challenge
"""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import norm, skew

plt.style.use("ggplot")

# file_path = "\challenge_1"
win_path = "D:/Learning/Projects/sds_challenges/challenge_1/data/public_flights.csv"
mac_path = "~/Projects/sds_challenge/challenge_1/data/public_flights.csv"
flight = pd.read_csv(win_path)

print(flight.columns)

print(flight.info())

# EDA
def missing_value_table(df):
    mis_val = df.isnull().sum()
    mis_val_pct = round(df.isnull().sum() * 100 / len(df), 2)
    
    # concatenate two columns
    mis_val_tbl = pd.concat([mis_val, mis_val_pct], axis = 1)
    
    # Rename columns 
    mis_val_tbl = mis_val_tbl.rename(columns = {0:"num NAs", 1:"pct NAs"})
    
    print(mis_val_tbl)
    
missing_value_table(flight)

# Explore column types
flight.dtypes.value_counts()

# Find unique values of each categorical columns
flight.select_dtypes('object').apply(pd.Series.nunique, axis = 0)



# function to print 
def autolabel(rects, col):
    for i, p in enumerate(rects.patches):
        height = p.get_height()
        rects.text(p.get_x()+p.get_width()/2., height + 0.2,\
            flight[col].value_counts()[i], ha = "center")


# VARIABLE: CANCELLED
flight["CANCELLED"].value_counts()

# Barplot with labels on top
ax = sns.countplot(data = flight, x = "CANCELLED")
autolabel(ax, "CANCELLED")


# VARIABLE: YEAR
flight["YEAR"].value_counts()

# VARIABLE: MONTH
flight["MONTH"].value_counts()
sns.countplot(data = flight, x = "MONTH")

# VARIABLE: DAY
flight["DAY"].value_counts()
sns.countplot(data = flight, x = "DAY")

# VARIABLE: Week of Day
flight["DAY_OF_WEEK"].value_counts()
sns.countplot(data = flight, x = "DAY_OF_WEEK")

# VARIABLE: AIRLINE
flight["AIRLINE"].value_counts()
sns.countplot(data = flight, x = "AIRLINE")

# VARIABLE: ORIGIN_AIRPORT
flight["ORIGIN_AIRPORT"].value_counts()
sns.countplot(data = flight, x = "ORIGIN_AIRPORT")

# VARIABLE: ORIGIN_AIRPORT
flight["DESTINATION_AIRPORT"].value_counts()
sns.countplot(data = flight, x = "DESTINATION_AIRPORT")

# VARIABLE: DISTANCE
sns.distplot(flight["DISTANCE"], fit=norm)
(mu, sigma) = norm.fit(flight["DISTANCE"])

# take log on DISTANCE
flight["LOG_DISTANCE"] = np.log(flight["DISTANCE"])
sns.distplot(flight["LOG_DISTANCE"], fit=norm)

# VARIABLE: SCHEDULED_TIME
sns.distplot(flight["SCHEDULED_TIME"], fit = norm)
(mu, sigma) = norm.fit(flight["SCHEDULED_TIME"].dropna())

# take log on SCHEDULED_TIME
flight["LOG_SCHEDULED_TIME"] = np.log(flight["SCHEDULED_TIME"])
sns.distplot(flight["LOG_SCHEDULED_TIME"], fit=norm)

# Make new variable
flight["ACTUAL_TIME"] = flight["SCHEDULED_ARRIVAL"] - flight["SCHEDULED_DEPARTURE"]

# ACTUAL_TIME vs SCHEDULED_TIME
sns.relplot(data = flight, kind = 'scatter', x = "SCHEDULED_TIME", y = "ACTUAL_TIME", hue = "CANCELLED")




























