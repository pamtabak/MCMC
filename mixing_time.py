import numpy as np
import random as rm
import matplotlib.pyplot as plt
import math

def prepare_ring_data (number_of_nodes):
	#preparing data
	states = []
	transitions = []
	pi = []
	for i in range(0, number_of_nodes):
		states.append(i)
		pi.append(0)
		prob = []
		for j in range (0, number_of_nodes):
			if (i == j):
				prob.append(0.5)
			elif (j == i - 1 or j == i + 1 or (i == 0 and j == number_of_nodes - 1) or (i == number_of_nodes - 1 and j == 0)):
				prob.append(0.25)
			else:
				prob.append(0)
		transitions.append(prob)
	return (states, transitions, pi)

def generate_binary_tree (number_of_nodes, exponential):
	matrix = []
	for i in range(0, number_of_nodes):
		matrix.append([])

	nodes = []
	nodes.append([0])
	for i in range(1, exponential):
		line = []
		for j in range(2**i - 1, 2**(i+1) - 1):
			line.append(j)
		nodes.append(line)
	for tree_line in range (0, len(nodes) - 1):
		current_node = 0
		it = 0
		for n in range(0, len(nodes[tree_line + 1])):
			matrix[nodes[tree_line + 1][n]].append(nodes[tree_line][current_node])
			matrix[nodes[tree_line][current_node]].append(nodes[tree_line + 1][n])
			it += 1
			if (it == 2):
				it = 0
				current_node += 1
	return matrix

def prepare_binary_tree_data (number_of_nodes, exponential):
	#preparing data
	states = []
	transitions = []
	pi = []
	binary_tree = generate_binary_tree (number_of_nodes, int(exponential))
	number_of_edges = 0

	for i in range(0, number_of_nodes):
		states.append(i)
		pi.append(0)
		prob = []
		for j in range (0, number_of_nodes):
			if (i == j):
				prob.append(0.5)
			else:
				if (j in binary_tree[i]):
					#there`s a edge between i and j. we need to know i`s degree
					number_of_edges += 1
					if (len(binary_tree[i]) == 1):
						prob.append(0.5)
					elif (len(binary_tree[i]) == 2):
						prob.append(0.25)
					elif (len(binary_tree[i]) == 3):
						prob.append (1.0 / 6)
				else:
					prob.append(0)
		transitions.append(prob)
	return (states, transitions, pi, binary_tree, number_of_edges)

def create_grid_2d (number_of_nodes):
	matrix = []
	for i in range(0, number_of_nodes):
		matrix.append([])
	lines = []
	for i in range(0, math.sqrt(number_of_nodes)):
		line = []
		for j in range(0, math.sqrt(number_of_nodes)):
			line.append(i*math.sqrt(number_of_nodes) + j)
			if (j < (math.sqrt(number_of_nodes) - 1)):
				matrix[i*math.sqrt(number_of_nodes) + j].append(i*math.sqrt(number_of_nodes) + j + 1)
				matrix[i*math.sqrt(number_of_nodes) + j + 1].append(i*math.sqrt(number_of_nodes) + j)
		lines.append(line)
	for l in range(0, len(lines) - 1):
		for element in range(0, len(lines[l])):
			matrix[lines[l][element]].append(lines[l+1][element])
			matrix[lines[l+1][element]].append(lines[l][element])
	return matrix

def prepare_grid_data (number_of_nodes):
	states = []
	transitions = []
	pi = []
	grid = create_grid_2d()
	for i in range (0, number_of_nodes):
		states.append(i)
		pi.append(0)
		prob = []
		for j in range (0, number_of_nodes):
			if (i == j):
				prob.append(0.5)
			elif (j in grid[i]):
				if (len(grid[i]) == 2):
					prob.append(0.25)
				if (len(grid[i]) == 3):
					prob.append(1.0/6)
				if (len(grid[i]) == 4):
					prob.append(1.0/8)
			else:
				prob.append(0)
		transitions.append(prob)
	return (states, transitions, pi, grid)

def run_ring_markov_chain (number_of_nodes):
	variation   = 1.0
	mixing_time = 0
	stationary_distribution = []
	for i in range(0, number_of_nodes):
		stationary_distribution.append(1.0/number_of_nodes)

	ring_data    = prepare_ring_data (number_of_nodes)
	states       = ring_data[0]
	transitions  = ring_data[1]
	pi           = ring_data[2]
	pi[0]        = 1
	current_node = 0

	while (variation > 0.000001):
		mixing_time += 1
		next_node = np.random.choice(states,replace=True,p=transitions[current_node])
		pi = np.matmul(pi, transitions)
		current_node = next_node
		v = 0
		for i in range (0, len(pi)):
			v += math.fabs ((stationary_distribution[i] - pi[i]))
		variation = v/2
	return mixing_time

def run_binary_tree_markov_chain (number_of_nodes):
	data   					= prepare_binary_tree_data(number_of_nodes, math.log(number_of_nodes + 1, 2))
	states 					= data[0]
	transitions 			= data[1]
	pi                      = data[2]
	pi[number_of_nodes - 1] = 1.0
	binary_tree_data 		= data[3]
	variation   			= 1.0
	stationary_distribution = []
	mixing_time 			= 0
	current_node 			= number_of_nodes - 1 #we are starting at last node
	print(data[4])
	for i in range(0, number_of_nodes):
		stationary_distribution.append(len(binary_tree_data[i])*1.0/data[4])
	while (variation > 0.000001):
		mixing_time += 1
		next_node = np.random.choice(states,replace=True,p=transitions[current_node])
		pi = np.matmul(pi, transitions)
		current_node = next_node
		v = 0
		for i in range (0, len(pi)):
			v += math.fabs ((stationary_distribution[i] - pi[i]))
		variation = v/2
	return mixing_time

# def run_grid_markov_chain (time):
# 	data = prepare_grid_data()
# 	states = data[0]
# 	transitions = data[1]
# 	first_pi = data[2]
# 	grid = data[3]
# 	variation = []
# 	stationary_distribution = []
# 	# precisa pegar numero de arestas
# 	for i in range(0, 1024):
# 		stationary_distribution.append(len(grid[i])*1.0/3968)
# 	for t in time:
# 		print("working at " + str(t))
# 		pi = grid_2d (t, states, transitions, first_pi, grid)
# 		v = 0
# 		for i in range (0, len(pi)):
# 			v += math.fabs ((stationary_distribution[i] - pi[i]))
# 		v = v/2
# 		variation.append(v)
# 		print(v)
# 	return variation

# ring_number_of_nodes = [10, 50, 100, 300, 700, 1000, 3000, 5000, 10000]
# ring_mixing_time = []
# for n in ring_number_of_nodes:
# 	ring_mixing_time.append(run_ring_markov_chain(n))
# tree_number_of_nodes = [7, 15, 63, 127, 255, 511, 1023, 2047, 4095, 8191]
tree_number_of_nodes = [1023]
tree_mixing_time = []
for n in tree_number_of_nodes:
	tree_mixing_time.append(run_binary_tree_markov_chain(n))
plt.plot(mixing_time, number_of_nodes, 'ro')
plt.xlabel('Tempo de Mistura')
plt.ylabel('Numero de Nos')
plt.show()