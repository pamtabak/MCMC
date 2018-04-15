import random
import math
import matplotlib.pyplot as plt
import numpy as np

def generate_samples():
	sample_sizes  = [1, 10, 100, 1000, 10000, 50000, 100000, 150000, 200000, 250000, 300000, 350000, 400000, 450000, 500000, 550000, 600000,
	 650000, 700000, 750000, 800000, 850000, 900000, 950000, 1000000 ]
	sample_values = []
	for s in sample_sizes:
		samples = []
		for i in range(0, s):
			sum_n = 0.0
			n = 0
			while (sum_n <= 1.0):
				sum_n += random.uniform(0, 1)
				n += 1
			samples.append(n)
		sample_values.append((1.0 * np.sum(samples))/len(samples))
	return (sample_sizes, sample_values)

def sample_mean ():
	samples = generate_samples()
	plt.plot(samples[0], samples[1], 'bo')
	plt.ylabel('Media Amostral')
	plt.xlabel('Numero de Amostras')
	plt.show()

def error ():
	e       = 2.71828
	samples = generate_samples()
	sample_sizes = samples[0]
	sample_relarive_errors = []
	sample_standard_errors = []
	for i in samples[1]:
		sample_relarive_errors.append(math.fabs(i - e)/e)
		sample_standard_errors.append((i - e)**2)

	plt.plot(sample_sizes, sample_relarive_errors, 'bo', label="relativo")
	plt.plot(sample_sizes, sample_standard_errors, 'ro', label="padrao")
	plt.xscale('log')
	plt.yscale('log')
	plt.show()

error()