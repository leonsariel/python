# _*_ coding: utf-8 _*_
__author__ = 'Di Meng'
__date__ = '1/13/2018 7:29 PM'
import pandas as pd
import numpy as np

#init a DF
dates = pd.date_range('20130101', periods=6)
df = pd.DataFrame(np.arange(24).reshape((6,4)), index=dates, columns=['A','B','C','D'])
print(df)

# select column A
print(df.A)

# slice first 3 rows
print(df[0:3])

# or slice by values
print(df['20130102':'20130104'])


