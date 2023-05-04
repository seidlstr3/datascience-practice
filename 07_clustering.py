#Three lines to make our compiler able to draw:
import sys
import matplotlib
matplotlib.use('Agg')

import pandas as pd
import matplotlib.pyplot as plt
import sklearn

from sklearn.cluster import KMeans
from sklearn import datasets

iris = datasets.load_iris()
iris_df = pd.DataFrame(iris.data)
iris_df.columns=['Sepal_Length', 'Sepal_Width', 'Petal_Length', 'Petal_Width']

print(iris_df.describe())
print(iris_df.head())

X=sklearn.preprocessing.scale(iris.data)
y=pd.DataFrame(iris.target)
variable_names = iris.feature_names

#print(X[0:10,])
#print(iris)


clustering = KMeans(n_clusters=10, random_state=5)
clustering.fit(X)


## Output
#print(iris_df.head())
x=iris_df.loc[:,'Petal_Length']
y=iris_df.loc[:,'Petal_Width']

plt.scatter(x=x,y=y)

#Two  lines to make our compiler able to draw:
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()
