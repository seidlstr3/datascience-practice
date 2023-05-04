#Three lines to make our compiler able to draw:
import sys
import matplotlib
matplotlib.use('Agg')

import pandas as pd
import matplotlib.pyplot as plt
import sklearn
import numpy as np


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

N=3
clustering = KMeans(n_clusters=N, random_state=5)
clustering.fit(X)


## Output
#print(iris_df.head())
x=iris_df.loc[:,'Petal_Length']
y=iris_df.loc[:,'Petal_Width']

print(iris.target)


colorz = np.random.randint(0,3,len(x))
#iris_df[]
#colorz=color_theme[iris.target]

my_map = plt.get_cmap('viridis', 3)

#########################################################

plt.subplot(1,2,1)

plt.scatter(x=x,y=y, c=iris.target, cmap=my_map)


plt.subplot(1,2,2)

#mapped_colors= np.vectorize(clustering.labels_.map({0:1, 1:0, 2:2})
mapped_colors = np.choose(clustering.labels_, [1,0,2]).astype(np.int64)

plt.scatter(x=x,y=y, c=mapped_colors, cmap= plt.get_cmap('viridis', N))


#Two  lines to make our compiler able to draw:
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()
