import pandas as pd
import numpy as np


#titanic = pd.read_csv("data/titanic.csv")
#ages = titanic["Age"]
#print(ages.head())

def line():
  print("-"*50)

# make it deterministic:
np.random.seed(0)

#data = np.random.rand(7*3).reshape(7,3)
data = np.random.randint(0,10,(7,3))

print(data)


line()

data_df = pd.DataFrame(data, columns=['pre', 'tmp', 'hum'])

print(data_df)

print(data_df.describe())

line()


print(data_df.loc[0])
print(data_df.loc[:,'tmp'])
print(type(data_df.loc[:,'tmp']))
