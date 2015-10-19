import math
import random
from helper import*

class Scout:
	def __init__(self):
		self.position = None
		self.fitness = None
		self.foragers = []
		self.patchside = 10
		self.num_cycles = 0

	def set_bee_position(self, bee_list, domain, rangey):
		#make it so two scouts cant be too close to each other
		#clean up code
		x_pos = domain[0]+ random.random()*(domain[1] - domain[0])
		y_pos = rangey[0]+ random.random()*(rangey[1] - rangey[0])
		# while [x_pos, y_pos] in [b.position for b in bee_list]:
		# 	x_pos = random.randint(domain[0], domain[1])
		# 	y_pos = random.randint(rangey[0], rangey[1])
		# 	print "overlapping position"
	 	self.position = [x_pos, y_pos]

	def domain(self):
		return [self.position[0] - self.patchside, self.position[0] + self.patchside]

	def rangey(self):
		return [self.position[1] - self.patchside, self.position[1] + self.patchside]

	def get_fitness(self): 
		self.fitness = 4000 - 100 * (self.position[0]**2 - self.position[1])**2 - (1 -self.position[0])**2
		return self.fitness

	def local_search(self):
		fitnesses = [f.get_fitness() for f in self.foragers]
		sorted_foragers= sorted(self.foragers, key = lambda f : f.fitness)
		if sorted_foragers[0].fitness > self.fitness:
			self.new_position(sorted_foragers[0].position)  #transfer leadership, move position of scout
			sorted_foragers[0].position = self.position #not sure we have to do this, but probably good practice

	def new_position(self, position):
		self.position = position
		self.num_cycles = 0

	def shrink_patch(self):
		self.patchside -= 1

	def generate_foragers(self, num_foragers, bee_list):
		forager_list = []
		domain = self.domain()
		rangey = self.rangey()

		if domain[0] < DOMAIN[0]:
			domain[0] = DOMAIN[0]
		if domain[1] > DOMAIN[1]:
			domain[1] = DOMAIN[1]

		if rangey[0] < RANGEY[0]:
			rangey[0] = RANGEY[0]
		if rangey[1] > RANGEY[1]:
			rangey[1] = RANGEY[1]		

		for i in range(num_foragers):
			forager = Forager(self)
			position_forager = forager.set_bee_position(bee_list, domain, rangey)
			forager_list.append(forager)
			bee_list.append(forager)

		self.foragers = forager_list

	def reset(self):
		self.position = None
		self.fitness = None
		self.foragers = []
		self.patchside = 10
		self.num_cycles = 0


class Forager(Scout):
	def __init__(self, scout):
		self.scout = scout
		self.position = None
		self.fitness = None
