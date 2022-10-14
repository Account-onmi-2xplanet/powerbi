import pandas as pd
from pandas_datareader import data as web
import matplotlib.pyplot as plt
dataset = web.DataReader(f'^BVSP', data_source='yahoo', start=f'02-20-2020', end=f'02-20-2021')
dataset['Amplitude'] = dataset['High'] - dataset['Low']
dataset['Date'] = dataset.index 
  
