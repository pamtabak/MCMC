import random
import math
import numpy as np
import matplotlib.pyplot as plt

def exact_sum (N):
	value = 0
	for i in xrange(1, N + 1):
		value += (i * math.log(i))
	return value

def get_k():
	k = 0
	for i in xrange(1, 1001):
		k += i**(1.15)
	return k

def get_y_values (k):
	values 		= []
	probability = []
	for i in xrange(1, 1001):
		values.append(i)
		probability.append(i**1.15/k)

	return (values, probability)

def estimated_sum (n, k, y_values, y_probabilities):
	# sequência da variável aleatória Y
	sequence = np.random.choice(y_values, n, replace=True, p=y_probabilities)
	value    = 0
	for i in xrange(1, n + 1):
		value += (sequence[i - 1] * math.log(sequence[i - 1]))/(sequence[i - 1]**1.15)
	value = (k/n) * value
	return value

samples = [1, 10, 100, 1000, 10000, 50000, 100000, 200000, 250000, 300000, 400000, 500000, 600000,
700000, 750000, 800000, 900000, 1000000]
errors   = []
k        = get_k()
y_values = get_y_values(k)
values   = y_values[0] #valores que y pode assumir
probability = y_values[1] #probabilidade de y assumir o valor da posição do array de cima
exact_sum_value = exact_sum(1000) #soma exata quando n igual a 1000

for s in samples:
	error = math.fabs(estimated_sum(s, k, values, probability) - exact_sum_value)/exact_sum_value
	errors.append(error)

plt.plot(samples, errors, 'bo')
plt.ylabel('Erro relativo')
plt.xlabel('Numero de Amostras')
plt.show()