""" lec_pd_datetime.py

Companion codes for the lecture on working with time-series data in Pandas
"""
import os
import datetime as dt

from lectures import toolkit_config as cfg

CSVLOC = os.path.join(cfg.DATADIR, 'tsla_prc.csv')

#x = dt.datetime(2023,12,31,9,30,33)
#y = x.strftime('%Y')
#print(f'Sunday of week number 53 of the year {y} ')

x = dt.datetime(2023,12,31,9,30,33)
y = x.strftime('%A of week number %U of the year %Y')
print(y)
