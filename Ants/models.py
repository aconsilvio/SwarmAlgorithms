import random

class Node:

	def __init__(self, value, index):
		self.value = value
		self.edges = []
		self.index = index

class Edge:
	def __init__(self, node1, node2):
		self.node1 = node1
		self.node2 = node2
		self.weight = 0
	
class Ant:
	def __init__(self, home):
		self.current_path = [home]
		self.is_forward = True

			




# tasks:
# create ants
# move an ant from one node to another
# move an ant again 
# check if node has food
# return on same trail
# lay down phers on way back
# at the origin, figure out where to go based on weighted probabilities


# ant class