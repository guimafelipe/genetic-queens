from state import *
import random

class Population:
    def __init__(self, k, n, elite):
        self.states = []
        self.n = n
        self.k = k
        self.elitesz = elite
        self.generate_random()

    def generate_random(self):
        random.seed()
        for i in range(self.k):
            values = []
            for j in range(self.n):
                values.append(random.randrange(0, self.n))
            self.states.append(State(self.n, values))

    def cross_over(self):
        # sorted(self.states, self.get_fitness, True)
        weigths = []
        wsum = 0
        for i in range(len(self.states)):
            weigths.append(self.states[i])
            wsum += self.states[i]
        for i in range(len(weigths)):
            weigths[i] /= wsum
    
    def get_fitness(self, x):
        return x.fitness()
    

