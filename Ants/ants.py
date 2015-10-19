from models import *
import random

Graph = [[0, 1, 0, 0, 1], [1, 0, 1, 1, 0], [0, 1, 0, 0, 1], [0, 1, 0, 0, 1], [1, 0, 1, 1, 0]]

def initialize_nodes(value_list):
	nodes = []
	for i, val in enumerate(value_list):
		node = Node(val, i)
		nodes.append(node)
				
	return nodes

def initialize_ants(start_node, num_ants):
	ant_list = []
	for ant in range(num_ants):
		ant = Ant(start_node)
		ant_list.append(ant)

	return ant_list

def move_step(ant, nodes):
	if not ant.is_forward:
		move_backward(ant, nodes)
	else:
		move_forward(ant, nodes)

def move_backward(ant, nodes):
	from_node = ant.current_path.pop()
	to_node = ant.current_path[-1]
	Graph[from_node.index][to_node.index] += 1

def move_forward(ant, nodes):
	edge_list = []	
	current_node = ant.current_path[-1]
	edges = Graph[current_node.index]
	for i, weight in enumerate(edges):
		if weight:
			edge_list += [i]*weight
	new_position_index = random.choice(edge_list)
	new_position = nodes[new_position_index]
	ant.current_path.append(new_position)

def generate_random_ants(home_node):
	num_ants = random.randint(1, 10)
	ants = initialize_ants(home_node, num_ants)
	return ants

def check_food(ant):
	node_value = ant.current_path[-1].value
	if node_value:
		ant.is_forward = False
		print "got food"

def ant_algorithm(value_list, num_cycles):
	nodes = initialize_nodes(value_list)
	home_node_position = random.randint(0, len(value_list)-1)
	home_node = nodes[home_node_position]
	print "home_node",home_node.index
	ants = generate_random_ants(home_node)
	for i in range(num_cycles):
		for ant in ants:
			move_step(ant, nodes)
			if len(ant.current_path) == 1:		
				ants.remove(ant)
			else:
				check_food(ant)
			new_ants = generate_random_ants(home_node)
	ants += new_ants
	print Graph	

if __name__ == '__main__':
	value_list = [0, 0, 1, 0, 1]
	num_cycles = 5
	print Graph
	ant_algorithm(value_list, num_cycles)

	