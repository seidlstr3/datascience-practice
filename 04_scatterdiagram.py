#Three lines to make our compiler able to draw:
import sys
import matplotlib
matplotlib.use('Agg')



import numpy
import matplotlib.pyplot as plt


#rnd = numpy.random.uniform(0.0, 5.0, 100000)
rnd = numpy.random.normal(2.5, 1.4, 100000)


#x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
#y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

x = numpy.random.normal(5.0, 2.0, 1000)
y = numpy.random.normal(5.0, 1.0, 1000)

plt.scatter(x, y)
plt.show()



#Two  lines to make our compiler able to draw:
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()

