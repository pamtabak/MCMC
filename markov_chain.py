import numpy as np
import random as rm
import matplotlib.pyplot as plt
import math

def ring (max_t):
	#preparing data
	states = []
	transitions = []
	pi = []
	for i in range(0, 1000):
		states.append(i)
		pi.append(0)
		prob = []
		for j in range (0, 1000):
			if (i == j):
				prob.append(0.5)
			elif (j == i - 1 or j == i + 1 or (i == 0 and j == 999) or (i == 999 and j == 0)):
				prob.append(0.25)
			else:
				prob.append(0)
		transitions.append(prob)
	# starting at node 0
	pi[0] = 1
	current_node = 0
	for time in range (0, max_t):
		next_node = change = np.random.choice(states,replace=True,p=transitions[current_node])
		pi = np.matmul(pi, transitions)
		current_node = next_node
	return pi

def generate_binary_tree ():
	matrix = []
	for i in range(0, 1023):
		matrix.append([])
	
	nodes = []
	nodes.append([0])
	nodes.append([1,2])
	nodes.append([3,4,5,6])
	nodes.append(range(7, 15))
	nodes.append(range(15, 31))
	nodes.append(range(31, 63))
	nodes.append(range(63, 127))
	nodes.append(range(127, 255))
	nodes.append(range(255, 511))
	nodes.append(range(511, 1023))
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

def binary_tree (max_t):
	#preparing data
	states = []
	transitions = []
	pi = []
	binary_tree = generate_binary_tree()
	for i in range(0, 1023):
		states.append(i)
		pi.append(0)
		prob = []
		for j in range (0, 1023):
			if (i == j):
				prob.append(0.5)
			else:
				if (j in binary_tree[i]):
					#there`s a edge between i and j. we need to know i`s degree
					if (len(binary_tree[i]) == 1):
						prob.append(0.5)
					elif (len(binary_tree[i]) == 2):
						prob.append(0.25)
					elif (len(binary_tree[i]) == 3):
						prob.append (1.0 / 6)
				else:
					prob.append(0)
		transitions.append(prob)
	# starting at node 0
	pi[0] = 1
	current_node = 0
	for time in range (0, max_t):
		next_node = change = np.random.choice(states,replace=True,p=transitions[current_node])
		print (next_node)
		pi = np.matmul(pi, transitions)
		current_node = next_node
	return pi

def create_grid_2d():
	matrix = []
	for i in range(0, 1024):
		matrix.append([])
	# each line or column has 32 nodes
	lines = []
	for i in range(0, 32):
		line = []
		for j in range(0, 32):
			line.append(i*32 + j)
			if (j < 31):
				matrix[i*32 + j].append(i*32 + j + 1)
				matrix[i*32 + j + 1].append(i*32 + j)
		lines.append(line)
	for l in range(0, len(lines) - 1):
		for element in range(0, len(lines[l])):
			matrix[lines[l][element]].append(lines[l+1][element])
			matrix[lines[l+1][element]].append(lines[l][element])
	return matrix


def grid_2d (max_t):
	#preparing data
	states = []
	transitions = []
	pi = []
	grid = create_grid_2d()
	for i in range (0, 1024):
		states.append(i)
		pi.append(0)
		prob = []
		for j in range (0, 1024):
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
	# starting at node 0
	pi[0] = 1
	current_node = 0
	for time in range (0, max_t):
		next_node = change = np.random.choice(states,replace=True,p=transitions[current_node])
		pi = np.matmul(pi, transitions)
		current_node = next_node
	return pi
		
grid_2d(1)			

# time = [10, 100, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
# variation = []
# stationary_distribution = []
# for i in range(0, 1000):
# 	stationary_distribution.append(1.0/1000)

# for t in time:
# 	pi = ring(t)
# 	v = 0
# 	for i in range (0, len(pi)):
# 		v += math.fabs ((stationary_distribution[i] - pi[i]))
# 	v = v/2
# 	variation.append(v)
# plt.plot(variation, time, 'ro')
# plt.xscale('log')
# plt.yscale('log')
# plt.xlabel('Variacao')
# plt.ylabel('Tempo (discreto)')
# plt.show()
