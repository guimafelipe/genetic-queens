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
		for i in range(self.e):
			self.elite.append(self.states[i])
	
	def generate_random(self):
		random.seed()
		for i in range(self.k):
			values = []
			for j in range(self.n):
				values.append(random.randrange(0, self.n))
			self.states.append(State(self.n, values))
	
	def order(self):
		self.states = sorted(self.states, key=lambda state: state.fitness(), reverse = True)

	def random_select(self):
		weigths = []
		wsum = 0
		for i in range(len(self.states)):
			weigths.append(self.states[i].fitness())
			wsum += self.states[i].fitness()
		
		probs = []
		for i in range(2):
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

	def iteration(self):
		new_states = []

		self.order()
		self.update_elite()

		for i in range(math.floor((self.k - self.e)/2)):
			r = self.random_select()
			new_states.extend(self.reproduce(r[0], r[1]))

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

	def mutate(self, x):
		mut_prob = 0.2
		prob = random.random()
		if prob < mut_prob:
			i = random.randrange(0, self.n)
			x.values[i] = random.randrange(0, self.n)
	
	def update_elite(self):
		self.elite = []
		for i in range(self.e):
			self.elite.append(self.states[i])

if __name__ == "__main__":
	pop = Population(10, 8, 2)
	i = 0
	while ((i < 100) and pop.states[0].fitness() < 28):
		pop.iteration()
	
	print(pop.states[0])