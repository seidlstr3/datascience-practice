#Three lines to make our compiler able to draw:
import sys
import matplotlib
matplotlib.use('Agg')



import numpy
import matplotlib.pyplot as plt


#rnd = numpy.random.uniform(0.0, 5.0, 100000)
rnd = numpy.random.normal(2.5, 1.4, 100000)

#print(rnd)

mean = numpy.mean(rnd)
var = numpy.var(rnd)

print(f"mean={mean}, variance={var}")


plt.hist(rnd,100)
plt.show()



#Two  lines to make our compiler able to draw:
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()
