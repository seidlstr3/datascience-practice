import numpy

speed1 = [10,11,12,13,14,15]

print(numpy.mean(speed1))
print(numpy.std(speed1))
print(numpy.var(speed1))

print("-"*10)

speed2 = [9,11,12,13,14,16]

print(numpy.mean(speed2))
print(numpy.std(speed2))
print(numpy.var(speed2))

print("-"*10)


ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]

p25=numpy.percentile(ages, 25)
print(f"25-percentile: {p25}")

p50=numpy.percentile(ages, 50)
print(f"25-percentile: {p50}")

p75=numpy.percentile(ages, 75)
print(f"25-percentile: {p75}")



