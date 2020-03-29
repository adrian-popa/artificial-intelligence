import copy
import itertools
import random


class Individual:

    def __init__(self, size):
        self.__cells = [[[-1, -1] for _ in range(size)] for _ in range(size)]
        self.__size = size
        self.__generate_individual()

    def __generate_individual(self):
        for i in range(self.__size):
            self.__cells[i] = self.__generate_line()

    def __generate_line(self):
        line = [[-1, -1] for _ in range(self.__size)]
        self.__permutations = list(itertools.permutations(list(range(1, self.__size + 1))))
        p1 = random.choice(self.__permutations)
        p2 = random.choice(self.__permutations)
        for i in range(self.__size):
            line[i] = [p1[i], p2[i]]
        return line

    def crossover(self, other, prob_cross):
        n = self.__size
        child1 = Individual(n)
        child2 = Individual(n)
        for i in range(n):
            if prob_cross > random.random():
                child1.set_line(i, copy.deepcopy(self.__cells[i]))
                child2.set_line(i, copy.deepcopy(other.get_line(i)))
            else:
                child1.set_line(i, copy.deepcopy(other.get_line(i)))
                child2.set_line(i, copy.deepcopy(self.__cells[i]))
        return child1, child2

    def fitness(self):
        return self.__wrong_columns() + self.__duplicate_cells()

    def mutate(self, prob_mut):
        for i in range(self.__size):
            if prob_mut > random.random():
                random.shuffle(self.__cells[i])

    def get_line(self, i):
        return self.__cells[i][:]

    def set_line(self, i, values):
        self.__cells[i] = values

    def get_neighbours(self):
        neighbours = []
        for i in range(self.__size):
            perms = list(itertools.permutations(self.__cells[i]))
            for perm in perms:
                cpy = copy.deepcopy(self)
                cpy.set_line(i, perm)
                neighbours.append(cpy)
        return neighbours

    def __get_column(self, i):
        col = set()
        for row in self.__cells:
            col.add(row[i])
        return col

    def __wrong_columns(self):
        count = 0
        values = set(i + 1 for i in range(self.__size))
        for j in range(self.__size):
            values_from_s = set()
            values_from_t = set()
            for i in range(self.__size):
                values_from_s.add(self.__cells[i][j][0])
                values_from_t.add(self.__cells[i][j][1])
            if values_from_s != values or values_from_t != values:
                count += 1
        return count

    def __duplicate_cells(self):
        matrix = set()
        for i in range(self.__size):
            for j in range(self.__size):
                matrix.add(tuple(self.__cells[i][j]))
        return self.__size * self.__size - len(matrix)

    def __str__(self):
        string = ''
        for i in range(self.__size):
            for p in self.__cells[i]:
                string += str(p) + ' '
            string += '\n'
        return string
