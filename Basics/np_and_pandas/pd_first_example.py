# _*_ coding: utf-8 _*_
__author__ = 'Di Meng'
__date__ = '1/13/2018 6:39 PM'
import pandas as pd
import numpy as np

# create first series, the element now have index number start from 0
s = pd.Series([1, 3, 6, np.nan, 44, 1])
print(s)

# create 6 dates from 2017-01-01
dates = pd.date_range('20170101', periods=6)
print(dates)

# make first dataFrame( matrix alike)
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=['a', 'b', 'c', 'd'])
print(df)

# another way to create dataFrame
df2 = pd.DataFrame({'A': 1.,
                    'B': pd.Timestamp('20130102'),
                    'C': pd.Series(1, index=list(range(4)), dtype='float32'),
                    'D': np.array([3] * 4, dtype='int32'),
                    'E': pd.Categorical(["test", "train", "test", "train"]),
                    'F': 'foo'})
print(df2)

# find out the type
print(df2.dtypes)

# find index
print(df.index)

# make report  of a matrix Number Only!!!
print(df2.describe())

# sort by index, count down
print(df.sort_index(axis=1, ascending=False))

# sort by values with column = E
print(df2.sort_values(by='E'))
