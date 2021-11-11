# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 02:29:58 2021

@author: 44473
"""

import os
import pandas as pd
import numpy as np
os.chdir('E:/ASU--博士生--1/Industrial Engineering/2021 Spring/IEE 577/project/nflscrapR-data-master/nflscrapR-data-master/games_data/regular_season')

files=os.listdir(os.getcwd())

for data_name in files:
    data=pd.read_csv(data_name)
    n=data.shape[0]
    temp=[]
    for i in range(n):
        temp.append(data.loc[i,'home_team'] if data.loc[i,'home_score']>data.loc[i,'away_score'] else data.loc[i,'away_team'])
    data['Win_Team']=temp
    data.to_csv('Win_Team_'+data_name,index=False,sep=',')