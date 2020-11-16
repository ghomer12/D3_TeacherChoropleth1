#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 23:13:58 2020

@author: greerhomer
"""

import pandas as pd
import numpy as np
import os

os.listdir()

#load data on teacher demographs from 2011–2012
teacher_demog = pd.read_csv('TeacherDemog.csv')

#get a list of headers
headers = teacher_demog.columns

#check for n/as
teacher_demog.isna().sum()
teacher_demog['Unnamed: 9'] #nothing is in this column
teacher_demog['Total Population'] #has issues with characters: commas and ‡

#drop last column that doesn't contain values
df_clean = teacher_demog.drop(columns=['Unnamed: 9'])
df_clean = df_clean.replace(r'\\n',' ', regex=True) 


#replace symbols with 0
df_clean = df_clean.replace('‡', 0)
df_clean = df_clean.replace('#', 0)

df_clean['Total Population'] = df_clean['Total Population'].str.replace(',', '').astype(float)
df_clean['Total Population'] = df_clean['Total Population'].fillna(0)
df_clean['Total Population'] = df_clean['Total Population'].astype(int)

#export clean data to csv
df_clean.to_csv('TeacherDemog_clean.csv', index=False)


