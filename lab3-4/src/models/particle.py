import copy
import itertools
import random


class Particle:

    def __init__(self, n, v_min, v_max):
        self.__n = n
        self.__velocity = [[random.randint(v_min, v_max), random.randint(v_min, v_max)] for _ in range(n)]
        self.__cells = [[[-1, -1] for _ in range(n)] for _ in range(n)]
        self.generate_individual()
        self.__bestPosition = copy.deepcopy(self)
        self.__bestFitness = self.fitness()

    def generate_individual(self):
        for i in range(self.__n):
            self.__cells[i] = self.__generate_line()

    def __generate_line(self):
        line = [[-1, -1] for _ in range(self.__n)]
        self.__permutations = list(itertools.permutations(list(range(1, self.__n + 1))))
        p1 = random.choice(self.__permutations)
        p2 = random.choice(self.__permutations)
        for i in range(self.__n):
            line[i] = [p1[i], p2[i]]
        return line

    def get_line(self, i):
        return self.__cells[i][:]

    def set_line(self, i, values):
        self.__cells[i] = values

    def get_line_from_s(self, i):
        values = []
        for j in range(self.__n):
            values.append(self.__cells[i][j][0])
        return values

    def get_line_from_t(self, i):
        values = []
        for j in range(self.__n):
            values.append(self.__cells[i][j][1])
        return values

    def set_line_from_s(self, i, new_line):
        for j in range(self.__n):
            self.__cells[i][j][0] = new_line[j]
        if self.fitness() < self.get_best_fitness():
            self.__bestFitness = self.fitness()
            self.__bestPosition = copy.deepcopy(self)

    def set_line_from_t(self, i, new_line):
        for j in range(self.__n):
            self.__cells[i][j][1] = new_line[j]
        if self.fitness() < self.get_best_fitness():
            self.__bestFitness = self.fitness()
            self.__bestPosition = copy.deepcopy(self)

    def fitness(self):
        return self.__wrong_columns() + self.__duplicate_cells()

    def get_neighbours(self, how_many):
        neighbours = []
        for i in range(self.__n):
            perms = list(itertools.permutations(self.__cells[i]))
            for perm in perms:
                cpy = copy.deepcopy(self)
                cpy.set_line(i, perm)
                neighbours.append(cpy)
        sorted(neighbours, key=lambda x: x.fitness())
        return neighbours[:how_many]

    def set_cells(self, cells):
        self.__cells = cells

    def get_velocity(self):
        return self.__velocity

    def get_best_fitness(self):
        return self.__bestFitness

    def get_best_position(self):
        return self.__bestPosition

    def __get_column(self, i):
        col = set()
        for row in self.__cells:
            col.add(row[i])
        return col

    def __wrong_columns(self):
        count = 0
        values = set(i + 1 for i in range(self.__n))
        for j in range(self.__n):
            values_from_s = set()
            values_from_t = set()
            for i in range(self.__n):
                values_from_s.add(self.__cells[i][j][0])
                values_from_t.add(self.__cells[i][j][1])
            if values_from_s != values or values_from_t != values:
                count += 1

        return count

    def __duplicate_cells(self):
        matrix = set()
        for i in range(self.__n):
            for j in range(self.__n):
                matrix.add(tuple(self.__cells[i][j]))
        return self.__n * self.__n - len(matrix)

    def __str__(self):
        string = ''
        for i in range(self.__n):
            for p in self.__cells[i]:
                string += str(p) + ' '
            string += '\n'
        return string
