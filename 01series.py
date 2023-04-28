import pandas as pd
import numpy as np
from pandas import Series, DataFrame

np.random.seed(25)
np.random.rand(10)

s = Series(np.random.rand(10))

s[[3]]=np.nan

s.fillna(23)

s.isnull().sum()

s.fillna(method='ffill')
