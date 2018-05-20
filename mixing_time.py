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
	number_of_lines = int(math.sqrt(number_of_nodes))
	for i in range(0, number_of_lines):
		line = []
		for j in range(0, number_of_lines):
			line.append(i*number_of_lines + j)
			if (j < (number_of_lines - 1)):
				matrix[i*number_of_lines + j].append(i*number_of_lines + j + 1)
				matrix[i*number_of_lines + j + 1].append(i*number_of_lines + j)
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
	grid = create_grid_2d (number_of_nodes)
	number_of_edges = 0
	for i in range (0, number_of_nodes):
		states.append(i)
		pi.append(0)
		prob = []
		for j in range (0, number_of_nodes):
			if (i == j):
				prob.append(0.5)
			elif (j in grid[i]):
				number_of_edges += 1
				if (len(grid[i]) == 2):
					prob.append(0.25)
				if (len(grid[i]) == 3):
					prob.append(1.0/6)
				if (len(grid[i]) == 4):
					prob.append(1.0/8)
			else:
				prob.append(0)
		transitions.append(prob)
	return (states, transitions, pi, grid, number_of_edges)

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
	#current_node = 0

	while (variation > 0.000001):
		mixing_time += 1
		#next_node = np.random.choice(states,replace=True,p=transitions[current_node])
		pi = np.matmul(pi, transitions)
		#current_node = next_node
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
	#current_node 			= number_of_nodes - 1 #we are starting at last node
	for i in range(0, number_of_nodes):
		stationary_distribution.append(len(binary_tree_data[i])*1.0/data[4])
	while (variation >= 0.000001):
		mixing_time += 1
		#next_node = np.random.choice(states,replace=True,p=transitions[current_node])
		pi = np.matmul(pi, transitions)
		#current_node = next_node
		v = 0
		for i in range (0, len(pi)):
			v += math.fabs ((stationary_distribution[i] - pi[i]))
		variation = v/2
	return mixing_time

def run_grid_markov_chain (number_of_nodes):
	data = prepare_grid_data(number_of_nodes)
	states = data[0]
	transitions = data[1]
	pi = data[2]
	grid = data[3]
	number_of_edges = data[4]
	variation = 0.0
	mixing_time = 0
	stationary_distribution = []
	for i in range(0, number_of_nodes):
		stationary_distribution.append(len(grid[i])*1.0/number_of_edges)
	while (variation >= 0.000001):
		mixing_time += 1
		#next_node = np.random.choice(states,replace=True,p=transitions[current_node])
		pi = np.matmul(pi, transitions)
		#current_node = next_node
		v = 0
		for i in range (0, len(pi)):
			v += math.fabs ((stationary_distribution[i] - pi[i]))
		variation = v/2
	return mixing_time

ring_number_of_nodes = [10, 50, 100, 300, 700, 1000, 3000, 5000, 10000]
ring_mixing_time = []
print("RING!!")
for n in ring_number_of_nodes:
	print(n)
	ring_mixing_time.append(run_ring_markov_chain(n))
tree_number_of_nodes = [7, 15, 63, 127, 255, 511, 1023, 2047, 4095, 8191]
print ("TREE!!")
tree_mixing_time = []
for n in tree_number_of_nodes:
	print(n)
 	tree_mixing_time.append(run_binary_tree_markov_chain(n))
grid_number_of_nodes = [8, 16, 64, 128, 256, 512, 1024, 2048, 4096, 8192]
print("GRID!!")
grid_mixing_time = []
for n in grid_number_of_nodes:
	print(n)
	grid_mixing_time.append(run_grid_markov_chain(n))
plt.plot(ring_mixing_time, ring_number_of_nodes, 'ro')
plt.plot(tree_mixing_time, tree_number_of_nodes, 'go')
plt.plot(grid_mixing_time, grid_number_of_nodes, 'bo')
plt.xlabel('Tempo de Mistura')
plt.ylabel('Numero de Nos')
plt.show()