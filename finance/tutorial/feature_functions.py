# _*_ coding: utf-8 _*_
__author__ = 'Di Meng'
__date__ = '1/3/2018 9:59 PM'

import pandas as pd
import numpy as np
from scipy import stats
import scipy.optimize
from scipy.optimize import OptimizeWarning
import warnings
import math
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from matplotlib.finance import _candlestick
from matplotlib.dates import date2num
from datetime import datetime


class holder:
    pass


# Heiken Ashi Candles
def candles(prices, periods):
    results = holder()
    dict = {}
    close = prices[['open', 'high', 'low', 'close']].sum(axis=1) / 4
    open = close.copy()
    open.iloc[0] = close.iloc[0]
    high = close.copy()
    low = close.copy()

    for i in range(1, len(prices)):
        open.iloc[i] = (open.iloc[i - 1] + close.iloc[i - 1]) / 2
        high.iloc[i] = np.array([prices.high.iloc[i], open.iloc[i], close.iloc[i]]).max()
        low.iloc[i] = np.array([prices.low.iloc[i], open.iloc[i], close.iloc[i]]).min()

    df = pd.concat((open, high, low, close), axis=1)
    df.columns = [['open', 'high', 'close', 'low']]

    # df.index = df.index.dropleve(0)
    dict[periods[0]] = df

    results.candles = dict

    return results


# Detrender
def detrend(prices, method='difference'):
    if method == 'difference':
        detrended = prices.close[1:] - prices.close[:-1].values
    elif method == 'linear':
        x = np.arange(0, len(prices))
        y = prices.close.values

        model = LinearRegression()
        model.fit(x.reshape(-1, 1), y.reshape(-1, 1))

        trend = model.predict(x.reshape(-1, 1))
        trend = trend.reshape((len(prices),))
        detrended = prices.close - trend

    else:
        print("error occurs")

    return detrended


# Fourier Series Expansion fitting Function fit sine cosine waves
def fSeries(x, a0, a1, b1, w):
    f = a0 + a1 * np.cos(w * x) + b1 * np.sin(w * x)
    return f


# Sine Series Expansion fitting Function fit sine cosine waves
def sSeries(x, a0, b1, w):
    f = a0 + b1 * np.sin(w * x)
    return f


def fourier(prices, periods, method='difference'):
    results = holder()
    dict = {}
    plot = True

    detrended = detrend(prices, method)
    for i in range(0, len(periods)):
        coeffs = []
        for j in range(periods[i], len(prices) - periods[i]):
            x = np.arange(0, periods[i])
            y = detrended.iloc[j - periods[i]:j]

            with warnings.catch_warnings():
                warnings.simplefilter('error', OptimizeWarning)

                try:
                    res = scipy.optimize.curve_fit(fSeries, x, y)
                except(RuntimeError, OptimizeWarning):
                    res = np.empty((1, 4))
                    res[0:] = np.NAN

            if plot == True:
                xt = np.linspace(0, periods[i], 100)
                yt = fSeries(xt, res[0][0], res[0][1], res[0][2], res[0][3])

                plt.plot(x, y)
                plt.plot(xt, yt, 'r')

                plt.show()

            coeffs = np.append(coeffs, res[0], axis=0)
        warnings.filterwarnings('ignore', category=np.VisibleDeprecationWarning)
        coeffs = np.array(coeffs).reshape(((len(coeffs) / 4, 4)))
        df = pd.DataFrame(coeffs, index=prices.iloc[periods[i]:-periods[i]])

        df.columns = [['a0', 'a1', 'b1', 'w']]
        df = df.fillna(method='bfill')
        dict[periods[i]] = df

    results.coeffs = dict
    return results


def sine(prices, periods, method='difference'):
    results = holder()
    dict = {}
    plot = False

    detrended = detrend(prices, method)
    for i in range(0, len(periods)):
        coeffs = []
        for j in range(periods[i], len(prices) - periods[i]):
            x = np.arrange(0, periods[i])
            y = detrended.iloc[j - periods[i]:j]

            with warnings.catch_warnings():
                warnings.simplefilter('error', OptimizeWarning)

                try:
                    res = scipy.optimize.curve_fit(sSeries, x, y)
                except(RuntimeError, OptimizeWarning):
                    res = np.empty((1, 3))
                    res[0:] = np.NAN

            if plot == True:
                xt = np.linspace(0, periods[i], 100)
                yt = sSeries(xt, res[0][0], res[0][1], res[0][2])

                plt.plot(x, y)
                plt.plot(xt, yt, 'r')

                plt.show()

            coeffs = np.append(coeffs, res[0], axis=0)
        warnings.filterwarnings('ignore', category=np.VisibleDeprecationWarning)
        coeffs = np.array(coeffs).reshape(((len(coeffs) / 3, 3)))
        df = pd.DataFrame(coeffs, index=prices.iloc[periods[i]:-periods[i]])

        df.columns = [['a0', 'b1', 'w']]
        df = df.fillna(method='bfill')
        dict[periods[i]] = df

    results.coeffs = dict
    return results


# Williams Accumulation Distribution Function
def wadl(prices, periods):
    results = holder()
    dict = {}
    l1 = len(periods)
    for i in range(0, l1):
        WAD = []
        for j in range(periods[i], len(prices) - periods[i]):
            # drop few in the begining
            trh = np.array([prices.high.iloc[j], prices.close.iloc[j - 1]]).max()
            trl = np.array([prices.low.iloc[j], prices.close.iloc[j - 1]]).min()

            if prices.close.iloc[j] > prices.close.iloc[j - 1]:
                PM = prices.close.iloc[j] - trl
            elif prices.close.iloc[j] < prices.close.iloc[j - 1]:
                PM = prices.close.iloc[j] - trh
            elif prices.close.iloc[j] == prices.close.iloc[j - 1]:
                PM = 0
            else:
                print("error")

            AD = PM * prices.volume.iloc[j]
            WAD = np.append(WAD, AD)
        WAD = WAD.cumsum()
        WAD = pd.DataFrame(WAD, index=prices.iloc[periods[i]:-periods[i]].index)
        WAD.columns = [['close']]
        dict[periods[i]] = WAD
    results.wadl = dict

    return results


# data resampling funciton
def OHLCresample(DataFrame, TimeFrame, column="ask"):
    grouped = DataFrame.groupby("Symbol")
    if np.any(DataFrame.columns == "Ask"):
        if column == "ask":
            ask = grouped['Ask'].resample(TimeFrame).ohlc()
            askVol = grouped['AskVol'].resample(TimeFrame).ohlc()
            resampled = pd.DataFrame(ask)
            resampled['AskVol'] = askVol

        elif column == 'bid':
            bid = grouped['Bid'].resample(TimeFrame).ohlc()
            bidVol = grouped['BidVol'].resample(TimeFrame).count()
            resampled = pd.DataFrame(bid)
            resampled['BidVol'] = bidVol
        else:
            raise ValueError('Column must be a string Either ask or bid')

    elif np.any(DataFrame.columns == "Close"):
        open = grouped['open'].resample(TimeFrame).ohlc()
        close = grouped['close'].resample(TimeFrame).ohlc()
        high = grouped['high'].resample(TimeFrame).ohlc()
        low = grouped['low'].resample(TimeFrame).ohlc()
        askVol = grouped['AskVol'].resample(TimeFrame).count()

        resampled = pd.DataFrame(open)
        resampled['high'] = high
        resampled['low'] = low
        resampled['close'] = close
        resampled['AskVol'] = askVol

    resampled = resampled.dropna()
    return resampled


# momentum
def momentum(prices, periods):
    results = holder()
    open = {}
    close = {}

    for i in range(0, len(periods)):
        open[periods[i]] = pd.DataFrame(prices.open.iloc[periods[i]:] - prices.open.iloc[:-periods[i]].values,
                                        index=prices.iloc[periods[i]:].index)
        close[periods[i]] = pd.DataFrame(
            prices.close.iloc[periods[i]:] - prices.close.iloc[:-periods[i]].values,
            index=prices.iloc[periods[i]:].index)
        open[periods[i]].columns = [['open']]
        close[periods[i]].columns = [['close']]

    results.open = open
    results.close = close
    return results


# stochastic

def stochastic(prices, periods):
    results = holder()
    close = {}

    for i in range(0, len(periods)):
        Ks = []
        for j in range(periods[i], len(prices) - periods[i]):
            C = prices.close.iloc[j + 1]
            H = prices.high.iloc[j - periods[i]:j].max()
            L = prices.low.iloc[j - periods[i]:j].min()

            if H == L:
                K = 0
            else:
                K = 100 * (C - L) / (H - L)
            Ks = np.append(Ks, K)

        df = pd.DataFrame(Ks, index=prices.iloc[periods[i] + 1:-periods[i] + 1].index)
        df.columns = [['K']]
        df['D'] = df.K.rolling(3).mean()
        df = df.dropna()
        close[periods[i]] = df

    results.close = close
    return results


# Williams %R
def williams(prices, periods):
    results = holder()
    close = {}

    for i in range(0, len(periods)):
        Rs = []
        for j in range(periods[i], len(prices) - periods[i]):
            C = prices.close.iloc[j + 1]
            H = prices.high.iloc[j - periods[i]:j].max()
            L = prices.low.iloc[j - periods[i]:j].min()

            if H == L:
                R = 0
            else:
                R = -100 * (H - C) / (H - L)

            Rs = np.append(Rs, R)
        df = pd.DataFrame(Rs, index=prices.iloc[periods[i] + 1:-periods[i] + 1].index)
        df.columns = [['R']]
        df = df.dropna()

        close[periods[i]] = df
    results.close = close
    return results


# price rate of change
def proc(prices, periods):
    results = holder()
    close = {}

    for i in range(0, len(periods)):
        proc[periods[i]] = pd.DataFrame(
            (prices.close.iloc[periods[i]:] - prices.close.iloc[:-periods[i]].values) / prices.close.iloc[
                                                                                        :-periods[i]].values)
        proc[periods[i]].columns = [['close']]
    results.proc = proc
    return results


# Accumulation distribution oscillator
def adosc(prices, periods):
    results = holder()
    accdist = {}

    for i in range(0, len(periods)):
        AD = []
        for j in range(periods[i], len(prices) - periods[i]):
            C = prices.close.iloc[j + 1]
            H = prices.high.iloc[j - periods[i]:j].max()
            L = prices.low.iloc[j - periods[i]:j].min()
            V = prices.AskVol.iloc[j + 1]

            if H == L:
                CLV = 0
            else:
                CLV = ((C - L) - (H - C)) / (H - L)
            AD = np.append(AD, CLV * V)
        AD = AD.cumsum()
        AD = pd.DataFrame(AD, index=prices.iloc[periods[i] + 1:-periods[i] + 1].index)
        AD.columns = [['AD']]

        accdist[periods[i]] = AD
        results.AD = accdist
        return results


# MACD
def macd(prices, periods):
    results = holder()
    EMA1 = prices.close.ewm(span=periods[0]).mean()
    EMA2 = prices.close.ewm(span=periods[1]).mean()

    MACD = pd.DataFrame(EMA1 - EMA2)
    MACD.columns = [['L']]

    sigMACD = MACD.rolling(3).mean()
    sigMACD.columns = [["SL"]]

    results.line = MACD
    results.signal = sigMACD

    return results


# CCI commodity channel index
def cci(prices, periods):
    results = holder()
    CCI = {}

    for i in range(0, len(periods)):
        MA = prices.close.rolling(periods[i]).mean()
        std = prices.close.rolling(periods[i]).std()
        D = (prices.close - MA) / std
        CCI[periods[i]] = pd.DataFrame((prices.close - MA) / (0.015 * D))
        CCI[periods[i]].columns = [['close']]
    results.cci = CCI
    return results


# Bollinger Bands
def bollinger(prices, periods, deviations):
    results = holder()
    boll = {}

    for i in range(0, len(periods)):
        mid = prices.close.rolling(periods[i]).mean()
        std = prices.close.rolling(periods[i]).std()
        upper = mid + deviations * std
        lower = mid - deviations * std

        df = pd.concat((upper, mid, lower), axis=1)
        df.columns = [['upper', 'mid', 'lower']]

        boll[periods[i]] = df
    results.bands = boll
    return results


# price average
def paverage(prices, periods):
    results = holder()
    avs = {}

    for i in range(0, len(periods)):
        avs[periods[i]] = pd.DataFrame(prices[['open', 'high', 'low', 'close']].rolling(periods[i]).mean())
    results.avs = avs
    return results


# slope function
def slopes(prices, periods):
    results = holder()
    slope = {}

    for i in range(0, len(periods)):
        ms = []
        for j in range(periods[i], len(prices) - periods[i]):
            y = prices.hgih.iloc[j - periods[i]:j].values
            x = np.arange(0, len(y))
            res = stats.lingregress(x, y=y)
            m = res.slope
            ms = np.append(ms, m)

        ms = pd.DataFrame(ms, index=prices.iloc[periods[i]:-periods[i]].index)
        ms.columns = [['high']]
        slope[periods[i]] = ms
    results.slope = slope
    return results
