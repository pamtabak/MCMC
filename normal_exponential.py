import random
import math
import matplotlib.pyplot as plt

lambda_value = 2

def exponential_sample ():
	random_number = random.uniform(0, 1)
	return math.log(lambda_value) - math.log(random_number)/lambda_value

def exponential_distribution (x):
	return lambda_value * math.exp(-lambda_value * x)

def normal_distribution (x):
	return 1.0/(math.sqrt(2*math.pi) * math.exp((-x**2)/2))

def rejection_sampling ():
	c = 1/(2 * math.sqrt(2*math.pi))
	while True:
		i = exponential_sample()
		j = exponential_distribution(i)
		if (random.uniform(0, c * j) < normal_distribution(i)):
			if (random.uniform(0,1) > 0.5):
				return (i, j)
			else:
				return (-i, j)

x = []
y = []
for i in range(0, 10000):
	tuple_values = rejection_sampling();
	x.append(tuple_values[0])
	y.append(tuple_values[1])
plt.plot(x, y, 'bo')
plt.xlabel('x')
plt.show()
#print(rejection_sampling())