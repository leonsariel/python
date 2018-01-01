from __future__ import print_function


import datetime
import statsmodels as ts
from pandas_datareader import data

amzn = data.DataReader(
    "AMZN", "yahoo",
    datetime.datetime(2007,1,1),
    datetime.datetime(2007,2,1)
)


print(amzn.tail())
ts.adfuller(amzn['Adj Close'],1)

#
# db = MySQLdb.connect("localhost","root","","securities_master")
# cursor = db.cursor()
# db.close()

