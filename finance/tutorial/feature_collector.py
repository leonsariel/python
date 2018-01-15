# _*_ coding: utf-8 _*_
__author__ = 'Di Meng'
__date__ = '1/13/2018 4:36 PM'

import pandas as pd
import numpy as np
from tutorial.feature_functions import *

# load our data
data = pd.read_csv('data/EURUSD_hours.csv')
data.columns = ['Date', 'open', 'high', 'low', 'close', 'volume']
data = data.set_index(pd.to_datetime(data.Date))

# delete the first date column
del data['Date']

# delete the duplicates for down time in market
prices = data.drop_duplicates(keep=False)

# create lists for each period required by our functions
momentum_key = [i for i in range(3, 11)]
stochastic_key = [i for i in range(3, 11)]
williams_key = [i for i in range(6, 11)]
proc_key = [i for i in range(12, 16)]
wadl_key = [15]
adosc_key = [i for i in range(2, 6)]
macd_key = [15, 30]
cci_key = [15]
bollinger_key = [15]
heikenashi_key = [15]
p_average_key = [2]
slope_key = [3, 4, 5, 10, 20, 30]
fourier_key = [10, 20, 30]
sine_key = [5, 6]

key_list = [momentum_key, stochastic_key, williams_key, proc_key, wadl_key, adosc_key, macd_key, cci_key, bollinger_key,
            heikenashi_key, p_average_key, slope_key]
#, fourier_key, sine_key

# calculate all features
momentum_dict = momentum(prices, momentum_key)
# print(momentum_dict.close)
print('1')
stochastic_dict = stochastic(prices, stochastic_key)
# print(stochastic_dict.close)
print('2')
williams_dict = williams(prices, williams_key)
# print(williams_dict.close)
print('3')
proc_dict = proc(prices, proc_key)
# print(proc_dict.proc)
print('4')
wadl_dict = wadl(prices, wadl_key)
# print( wadl_dict.wadl)
print('5')
adosc_dict = adosc(prices, adosc_key)
# print(adosc_dict.AD)
print('6')

macd_dict = macd(prices, macd_key)
# print(macd_dict.line)
print('7')
cci_dict = cci(prices, cci_key)
# print(cci_dict.cci)
print('8')
bollinger_dict = bollinger(prices, bollinger_key, 2)
# print( bollinger_dict.bands)
print('9')

hka_prices = prices.copy()
hka_prices['Symbol'] = 'SYMB'
HKA = OHLCresample(hka_prices, '15H')
heiken_dict = candles(HKA, heikenashi_key)
# print(heiken_dict.candles)
print('10')
paverage_dict = paverage(prices, p_average_key)
# print( paverage_dict.avs)
print('11')
slope_dict = slopes(prices, slope_key)
# print(slope_dict.slope)
print('12')
# fourier_dict = fourier(prices, fourier_key)
# # print('13')
# sine_dict = sine(prices, sine_key)
# # print(sine_dict.coeffs)
# print('14')

# create list of dictionaries
dict_list = [
    momentum_dict.close,
             stochastic_dict.close,
             williams_dict.close,
             proc_dict.proc,
             wadl_dict.wadl,
             adosc_dict.AD,
             macd_dict.line,
             cci_dict.cci,
             bollinger_dict.bands,
             heiken_dict.candles,
              paverage_dict.avs,
             slope_dict.slope]
            #  fourier_dict.coeffs,
            # sine_dict.coeffs]

feature_name = ['momentum', 'stoch', 'will', 'proc', 'wadl', 'adosc', 'macd', 'cci', 'bollinger', 'heiken', 'paverage',
                'slope']

# , 'fourier', 'sine']


# feature_name = feature_name[0:13]
# key_list = key_list[0:13]
# dict_list = dict_list[0:13]

master_frame = pd.DataFrame(index=prices.index)

for i in range(0, len(dict_list)):
    if feature_name[i] == 'macd':
        col_id = feature_name[i] + str(key_list[6][0] + key_list[6][1])
        master_frame[col_id] = dict_list[i]
    else:
        for j in key_list[i]:
            try:
                for k in dict_list[i][j]:
                    k = ''.join(k)
                    col_id = feature_name[i] + str(j) + str(k)

                    master_frame[col_id] = dict_list[i][j][k]
            except (KeyError, ValueError) as error:
                print("error on ", j)

threshold = round(0.7 * len(master_frame))
master_frame[['open', 'high', 'low', 'close']] = prices[['open', 'high', 'low', 'close']]

# Heiken Ashi is resampled , it will have empty value in between
# master_frame['heiken15open'] = master_frame.heiken15open.fillna(method='bfill')
# master_frame.heiken15high = master_frame.heiken15high.fillna(method='bfill')
# master_frame.heiken15low = master_frame.heiken15low.fillna(method='bfill')
# master_frame.heiken15close = master_frame.heiken15close.fillna(method='bfill')

# drop all cols that have 30% or more NAN data
master_frame_cleaned = master_frame.copy()
master_frame_cleaned = master_frame_cleaned.dropna(axis=1, thresh=threshold)
master_frame_cleaned = master_frame_cleaned.dropna(axis=0)

master_frame_cleaned.to_csv('data/master_frame.csv')
print("complete!")
