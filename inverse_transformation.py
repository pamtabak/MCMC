import random
import math

def exponential_function (random_uniform):
	lambda_value = 3
	return (math.log(lambda_value) - math.log(random_uniform)/lambda_value)

def pareto_function ():
	alpha_value = 5.0
	first_x     = 1.0
	x 			= 0

	y = random.uniform(0, 1)
	while (x < first_x):
		x = ((alpha_value*(first_x**alpha_value))/y)**(1/(alpha_value + 1))

	return x
	

result = ""
for i in range(0,20):
	#result += str(exponential_function(random.uniform(0, 1))) + ", "
	result += str(pareto_function()) + ", "

print(result)