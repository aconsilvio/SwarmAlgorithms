import helper
from models import*

bee_list = []

def intialize_scouts(num_scouts):
	scout_list = []
	for i in range(num_scouts):
		s = Scout()
		s.set_bee_position(bee_list, helper.DOMAIN, helper.RANGEY)
		scout_list.append(s)
		bee_list.append(s)
	return scout_list

def recruit(scouts, nse, nsb, nfe, nfb):
	fitnesses = [s.get_fitness() for s in scouts]
	sorted_s = sorted(scouts, key = lambda s : s.fitness)
	sorted_s.reverse()
	elite_scouts = sorted_s[0:helper.NSE]
	best_scouts = sorted_s[helper.NSE:helper.NSB+helper.NSE]
	global_scouts = sorted_s[helper.NSB+helper.NSE:]
	
	for scout in elite_scouts:
		scout.generate_foragers(helper.NFE, bee_list)

	for scout in best_scouts:
		scout.generate_foragers(helper.NFB, bee_list)
	return [elite_scouts + best_scouts, global_scouts]

def new_patch(scout):
	scout.reset()
	scout.set_bee_position(bee_list, helper.DOMAIN, helper.RANGEY)
	return scout

def bee_algorithm(scouts, n):
	if n > helper.MAX_CYCLES:
		fitnesses = [s.get_fitness() for s in scouts]
		sorted_s = sorted(scouts, key = lambda s : s.fitness)
		sorted_s.reverse()
		max_scout = sorted_s[0]
		#print (max_scout.fitness, max_scout.position)
		return_tuple = (max_scout.fitness, max_scout.position, scouts)
		return return_tuple

	if len(scouts) == 0:  #base case
		scouts = intialize_scouts(helper.NS)
	new_scouts = []
	ranked_scouts = recruit(scouts, helper.NSE, helper.NSB, helper.NFE, helper.NFB)
	for i, scout in enumerate(ranked_scouts[0]):
		new_scouts.append(scout)
		new_scouts[i].local_search()
		if new_scouts[i].position == scout.position:
			new_scouts[i].shrink_patch()
		elif scout.num_cycles > helper.NC:
			new_scouts[i] = new_patch(scout)

	for i, scout in enumerate(ranked_scouts[1]):  #set global scouts to new positions to be searched
		new_scout = new_patch(scout)
		new_scouts.append(new_scout)

	return bee_algorithm(new_scouts, n+1)





if __name__ == '__main__':
	#scouts = intialize_scouts(helper.NS)
	#print [s.position for s in scouts]
	#sr = recruit(scouts, helper.NSE, helper.NSB, helper.NFE, helper.NFB)
	# flattened = [scout for sub_sr in sr for scout in sub_sr]
	# foragers = [scout.foragers for scout in flattened]
	# print foragers
	bee_algorithm([],0)
