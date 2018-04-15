import random
import math
import matplotlib.pyplot as plt

k2 = 333833500

def exact_sum (N):
	value = 0
	for i in xrange(1, N + 1):
		value += (i * math.log(i))
	return value

def estimated_sum (n):
	value = 0
	for i in xrange(1, n + 1):
		value += math.log(i)/i
	value = (k2/n) * value
	return value

samples = [1, 10, 100, 1000, 10000, 50000, 100000, 200000, 250000, 300000, 400000, 500000, 600000,
700000, 750000, 800000, 900000, 1000000]
errors = []
exact_sum_value = exact_sum(1000)
for s in samples:
	error = math.fabs(estimated_sum(s) - exact_sum_value)/exact_sum_value
	errors.append(error)

plt.plot(samples, errors, 'bo')
plt.ylabel('Erro relativo')
plt.xlabel('Numero de Amostras')
plt.show()
