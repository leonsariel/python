# _*_ coding: utf-8 _*_
__author__ = 'Di Meng'
__date__ = '1/24/2018 2:38 PM'
import numpy
import talib
from talib import MA_Type


def test_SMA():
    close = numpy.random.random(100)
    output = talib.SMA(close,5)
    print(output)
close = numpy.random.random(100)
upper, middle, lower = talib.BBANDS(close, matype=MA_Type.T3)

print("this is upper: ", upper)
print("this is middle: ", middle)
print("this is lower: ", lower)