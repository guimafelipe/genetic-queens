from state import *
import random
import math

def get_fitness(x):
	return x.fitness()

class Population:
	def __init__(self, k, n, e):
		self.states = []
		self.n = n
		self.k = k
		self.e = e
		self.elite = []
		self.generate_random()
		self.generation = 0
		self.order()

	# Generate initial set, in O(n*k)
	def generate_random(self):
		random.seed()
		for i in range(self.k):
			values = []
			for j in range(self.n):
				values.append(random.randrange(0, self.n))
			self.states.append(State(self.n, values))

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

		self.order()
		self.update_elite()

		r = self.random_select(self.k - self.e)

		for i in range(0, self.k - self.e, 2):
			new_states.extend(self.reproduce(r[i], r[i+1]))

		self.states = new_states

		for el in self.elite:
			self.states.append(el)

		print(self.generation)
		self.generation+=1

		for el in self.states:
			self.mutate(el)
		
		for el in self.elite:
			self.states.append(el)
		
		self.order()

		print("Best: ", self.states[0])
		return new_states
	
	# Reproduce function, runs in O(n)
	def reproduce(self, a, b):
		vala = []
		valb = []
		cut = random.randrange(1, self.n-1)
		for i  in range(cut):
			vala.append(a.values[i])
			valb.append(b.values[i])
		for i in range(cut, self.n):
			vala.append(b.values[i])
			valb.append(a.values[i])
		resp = []
		na = State(self.n, vala)
		nb = State(self.n, valb)
		resp.append(na)
		resp.append(nb)
		return na, nb

	# Mutate function, runs in O(1)
	def mutate(self, x):
		mut_prob = 0.3
		prob = random.random()
		if prob < mut_prob:
			i = random.randrange(0, self.n)
			x.values[i] = random.randrange(0, self.n)
	
	# Update elite function, runs in O(e)
	def update_elite(self):
		self.elite = []
		for i in range(self.e):
			self.elite.append(self.states[i])

if __name__ == "__main__":
	n = 8
	k = 10
	e = 2
	pop = Population(k, n, e)
	while (pop.states[0].fitness() < ((n-1)*n)/2):
		pop.iteration()
	
	print(pop.states[0])