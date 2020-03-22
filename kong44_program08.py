#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 15:15:07 2020
@author: kong44

Program Description: 
    This script takes a TXT file input and plots the data. 
    The data is recorded discharge from the Wabash River. 
    
References: 
    https://www.earthdatascience.org/courses/use-data-open-source-python/use-time-series-data-in-python/date-time-types-in-pandas-python/resample-time-series-data-pandas-python/
    https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.date_range.html
    https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sort_values.html
"""

# module import 
import pandas as pd
import matplotlib.pyplot as plt

# loading in the data 
# date and time are a single element, used as the index
# discharged used as values of the index
discharge = pd.read_table('WabashRiver_DailyDischarge_20150317-20160324.txt',
                          parse_dates = True,
                          usecols = [2,4],
                          index_col = ['Date & Time'],
                          skiprows = 26,
                          names = ['Date & Time','Discharge']
                          )

# plot of daily average streamflow 
# resampling to daily data
daily_resample = discharge.resample("D").mean()
daily_avg_flow = daily_resample.plot(title='Daily Average Streamflow for the Wabash')
daily_avg_flow.set_xlabel('Date')
daily_avg_flow.set_ylabel('Discharge (cfs)')
daily_avg_flow.figure.savefig('Daily Average Flow.pdf')
plt.close()

# plotting the 10 days with the highest flow over the daily average
# sorting based on discharge
max_flow = daily_resample.sort_values(by =['Discharge'], ascending=False)
high_points = max_flow.iloc[0:10] # isolate top 10

daily_resample.plot(title='Daily Average Streamflow for the Wabash') # line
plt.scatter(high_points.index,high_points.Discharge,color='k') # points
plt.legend(['Daily Average Discharge','10 Highest Flows'])
plt.xlabel('Date')
plt.ylabel('Discharge (cfs)')
plt.savefig('Daily Average Flow & High Points.pdf')
plt.close()

# plot of monthly average streamflow 
month_resample = discharge.resample('M').mean()
month = month_resample.plot(title='Monthly Average Streamflow for the Wabash')
month.set_xlabel('Date')
month.set_ylabel('Discharge (cfs)')
month.figure.savefig('Monthly Average Flow.pdf')
plt.close()