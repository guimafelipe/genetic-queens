class State:
    def __init__(self, n, values):
        self.n = n
        self.values = values

    def __str__(self):
        return str(self.values)

    # now runs in O(n), happy
    def fitness(self):
        fit = 0

        lines = {}
        up_diagonals = {}
        low_diagonals = {}

        for i in range(self.n):
            if lines.get(self.values[i], -1) == -1:
                lines[self.values[i]] = 0
            lines[self.values[i]] += 1
        
        for i in range(self.n):
            diagonal = self.values[i] - i
            if up_diagonals.get(diagonal, -1) == -1:
                up_diagonals[diagonal] = 0
            up_diagonals[diagonal] += 1

        for i in range(self.n):
            diagonal = i + self.values[i]
            if low_diagonals.get(diagonal, -1) == -1:
                low_diagonals[diagonal] = 0
            low_diagonals[diagonal] += 1

        for val in lines.values():
            fit += (val*(val-1))/2

        for val in up_diagonals.values():
            fit += (val*(val-1))/2

        for val in low_diagonals.values():
            fit += (val*(val-1))/2

        fit = (self.n*(self.n-1))/2 - fit
        return fit

if __name__ == "__main__":
    s1 = State(8, [2,4,7,4,8,5,5,2])
    print(s1.fitness()) # 21
