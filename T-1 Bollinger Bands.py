# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 10:03:27 2018

@author: peirmah
"""

import pandas as pd
import matplotlib.pyplot as plt


file_path = r'Z:\Tech Smart Beta Project\Python\ML\Technical Models\BP.csv'

df = pd.read_csv(file_path)

date = []

def Bollinger_Band(price,window_size,num_std):
    rolling_mean = price.rolling(window=window_size).mean()
    rolling_std = price.rolling(window=window_size).std()
    upper_band = rolling_mean + (rolling_std*num_std)
    lower_band = rolling_mean - (rolling_std*num_std)
    date = pd.to_datetime(df['Date'])
    
    plt.plot(date,price,label=['SharePrice'])
    plt.plot(date,rolling_mean,label=['Rolling Mean'])
    plt.plot(date,upper_band,label=['+ band'])
    plt.plot(date,lower_band,label=['- band'])
    plt.xlabel('Date')
    plt.ylabel('USD')
    plt.legend()
    plt.show()
    



Bollinger_Band(df['Adj Close'],10,2)



