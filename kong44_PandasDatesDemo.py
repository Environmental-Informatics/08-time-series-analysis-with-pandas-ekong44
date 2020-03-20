#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 15:14:24 2020
@author: kong44

Program Description: 
Working through the tutorial on provided in - http://earthpy.org/pandas-basics.html

"""

# module import 
import pandas as pd
import matplotlib as plt
import numpy as np
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

