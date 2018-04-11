import random
import math
import matplotlib.pyplot as plt

def exponential_function ():
	lambda_value = 3
	x = []
	y = []
	for i in range(0, 200):
		random_number = random.uniform(0, 1)
		y.append(random_number)
		x.append(math.log(lambda_value) - math.log(random_number)/lambda_value)
	plt.plot(x, y, 'ro')
	plt.ylabel('Uniforme(0,1)')
	plt.xlabel('Valor da Inversa')
	plt.show()

def pareto_function ():
	alpha_value = 5.0
	first_x     = 1.0

	x = []
	y = []
	for i in range(0, 200):
		x_value 	  = 0
		random_number = random.uniform(0, 1)
		y.append(random_number)
		while (x_value < first_x):
			x_value = ((alpha_value*(first_x**alpha_value))/random_number)**(1/(alpha_value + 1))
		x.append(x_value)
	plt.plot(x, y, 'bo')
	plt.ylabel('Uniforme(0,1)')
	plt.xlabel('Valor da Inversa')
	plt.show()


#exponential_function()
pareto_function()