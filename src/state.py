
class State:
    def __init__(self, n, values):
        self.n = n
        self.values = values

    def __str__(self):
        return str(self.values)

    def crossover(self, ind):
        self.values[ind] = 5
    
    def fitness(self):
        fit = 0
        for i in range(self.n):
            for j in range(i+1, self.n):
                fit += self.atacking(i, j)
        return fit
    
    def atacking(self, i, j):
        if(self.values[i] == self.values[j]):
            return 0
        if(abs(i-j) == abs(self.values[i] - self.values[j])):
            return 0
        return 1

if __name__ == "__main__":
    s1 = State(8, [2,4,7,4,8,5,5,2])
    print(s1.fitness())
