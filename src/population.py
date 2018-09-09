from src.state import *
import random
import math

def get_fitness(x):
	return x.fitness()

class Population:
	def __init__(self, k, n, m):
		self.states = []
		self.n = n # board size
		self.k = k # population size
		self.m = m # mutation probability
		self.base = [i for i in range(self.n)]
		self.generate_random()
		self.generation = 0
		self.order()

	# Generate initial set, in O(n*k)
	def generate_random(self):
		random.seed()
		for i in range(self.k):
			random.shuffle(self.base)
			self.states.append(State(self.n, self.base))

	# Order funcion, runs in O(k.log(k))
	def order(self):
		self.states = sorted(self.states, key=lambda state: state.fitness(), reverse = True)

	# Random slection function, wich select 2 elements to reproduce
	# runs in O(k + nmb)
	def random_select(self, nmb):
		weigths = []
		wsum = 0
		for i in range(len(self.states)):
			weigths.append(self.states[i].fitness())
			wsum += self.states[i].fitness()
		
		probs = []
		for i in range(nmb):
			probs.append(random.randrange(0, wsum))
		probs = sorted(probs)
		currsum = 0
		j = 0
		i = 0
		r = []
		currsum += weigths[0]
		while i < len(weigths):
			if(currsum > probs[j]):
				r.append(self.states[i])
				j+=1
				if j >= len(probs):
					break
			else:
				i+=1
				if i < len(weigths):
					currsum += weigths[i]

		return r

	# Iterarion function, runs every new generation
	# Time complexity: O(k.log(k)) + O(e) + O(2*k-e) + O(e) + O(k) + 
	def iteration(self):
		new_states = []

		r = self.random_select(self.k)

		for i in range(0, self.k, 2):
			new_states.extend(self.reproduce(r[i], r[i+1]))

		self.states.extend(new_states)
		self.order()
		self.states = self.states[0:self.k]

		self.generation+=1
		
		for el in self.states:
			self.mutate(el)
			self.mutate(el)

		return new_states
	
	def crossover(self, cut1, cut2, inserted, values, valuesres):
		i = 0
		j = 0

		res = valuesres.copy()
		
		while i < cut1:
			while values[j] in inserted:
				j+=1
			res[i] = values[j]
			i+=1
			j+=1
		
		i = cut2
		while i < self.n:
			while values[j] in inserted:
				j += 1
			res[i] = values[j]
			i+=1
			j+=1
		return res

	# Reproduce function, runs in O(n)
	def reproduce(self, a, b):
		cut1 = random.randrange(0, self.n-1)
		cut2 = random.randrange(cut1 + 1, self.n)
		ainserted = a.values[cut1:cut2]
		binserted = b.values[cut1:cut2]

		vala = self.crossover(cut1, cut2, ainserted, b.values, a.values)	
		valb = self.crossover(cut1, cut2, binserted, a.values, b.values)

		resp = []
		na = State(self.n, vala)
		nb = State(self.n, valb)
		resp.append(na)
		resp.append(nb)
		return resp

	# Mutate function, runs in O(1)
	def mutate(self, x):
		prob = random.random()
		before_fit = x.fitness()
		if prob < self.m:
			i = random.randrange(0, self.n)
			j = random.randrange(0, self.n)
			aux = x.values[i]
			x.values[i] = x.values[j]
			x.values[j] = aux
			if before_fit > x.fitness():
				aux = x.values[i]
				x.values[i] = x.values[j]
				x.values[j] = aux
	
	def get_best(self):
		return self.states[0]

if __name__ == "__main__":
	n = 8
	k = 40
	e = 6
	m = 0.5
	pop = Population(k, n, m)
	s1 = State(n, [0,1,2,3,4,5,6,7])
	s2 = State(n, [7,6,5,4,3,2,1,0])
	res = pop.reproduce(s1, s2)
	for s in res:
		print (s.values)
	# while (pop.states[0].fitness() < ((n-1)*n)/2):
	# 	pop.iteration()
	
	# print(pop.states[0])