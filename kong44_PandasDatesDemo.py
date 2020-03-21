#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 15:14:24 2020
@author: kong44

Program Description: 
Working through the tutorial on provided in - http://earthpy.org/pandas-basics.html
Some of the code was ran through the console so that outputs could be seen.
In this script, we are using pandas and other modules to analyze time series. 
"""

# module import 
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime
from pandas import Series, DataFrame, Panel

# loading data
# data retrieved after command is entered into console
nao = np.loadtxt('norm.nao.monthly.b5001.current.ascii')
ao = np.loadtxt('monthly.ao.index.b50.current.ascii')

# convert this data to a time series 
dates = pd.date_range('1950-01', periods=ao.shape[0], freq='M') # create range of dates
dates_nao = pd.date_range('1950-01', periods=nao.shape[0], freq='M')

NAO = Series(nao[:,2], index=dates_nao)
AO = Series(ao[:,2], index=dates) # dates as index, oscillation as values

#plotting with Pandas
DAO = AO.plot(title='Daily Atlantic Oscillation (AO)')
DAO.set_xlabel('Year')
DAO.set_ylabel('Oscillation Index')
DAO.figure.savefig('Daily AO.pdf')
plt.close()

# other plots
AO['1980':'1990'].plot()
plt.show()
plt.close()
AO['1980-05':'1981-03'].plot()
plt.show()
plt.close()

# creating a DF with both data
aonao = DataFrame({'AO' : AO, 'NAO' : NAO})

#plot data
aonao.plot(subplots=True)
plt.show()
plt.close()

#add column to data frame
aonao['Diff'] = aonao['AO'] - aonao['NAO']

# deleting the column
del aonao['Diff']

# crazy combinations
aonao.loc[(aonao.AO > 0) & (aonao.NAO < 0) 
        & (aonao.index > datetime.datetime(1980,1,1)) 
        & (aonao.index < datetime.datetime(1989,1,1)),
        'NAO'].plot(kind='barh')
plt.show()
plt.close()

# statistical calculations done in the console 

# resampling with mean
AO_mm = AO.resample("A").mean()
AO_mm.plot(style='g--')
plt.show()
plt.close()

# resampling with median
AO_mm = AO.resample("A").median()
Annual_MedianAO = AO_mm.plot(title='Annual Median Atlantic Oscillation (AO)')
Annual_MedianAO.set_xlabel('Year')
Annual_MedianAO.set_ylabel('Oscillation Index')
Annual_MedianAO.figure.savefig('Annual Median AO.pdf')
plt.close()

# sampling frequency at 3 years
AO_mm = AO.resample("3A").apply(np.max)
AO_mm.plot()
AO_mm.plot(style='g--')
plt.show()
plt.close()

# specify several functions
AO_mm = AO.resample("A").apply(['mean', np.min, np.max])
AO_mm['1900':'2020'].plot(subplots=True)
AO_mm['1900':'2020'].plot()
plt.show()
plt.close()

# moving/rolling statistics 
roll = aonao.rolling(window=12, center=False).mean().plot(title='Rolling Mean for Arctic & North Atlantic Oscillation')
roll.set_xlabel('Year')
roll.set_ylabel('Oscillation Index')
roll.figure.savefig('Rolling Mean.pdf')
plt.close()