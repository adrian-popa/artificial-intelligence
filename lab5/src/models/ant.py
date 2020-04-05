from copy import deepcopy
from random import random, choice
import numpy as np


class Ant:

    def __init__(self, problem):
        self.__problem = problem
        self.__n = problem.get_size()
        self.__path = []
        self.__visited = []
        self.__numbers = np.random.permutation(self.__n)
        self.__graph_no = 0

    def update(self, trace, alpha, beta, q0):
        if not self.__visited:
            self.__visited.append(choice(self.__numbers))
        else:
            if len(self.__visited) == self.__n - 1:
                for number in self.__numbers:
                    if self.__is_node_visited(number) is False:
                        self.__visited.append(number)
                        self.__replace_graph()
                        break
            else:
                previous = self.__visited[-1]
                moves = self.__next_moves()
                moves_no = len(moves)

                product = [1 for _ in range(moves_no)]
                product = [(product[i] ** beta) * (trace[self.__graph_no][previous][moves[i]] ** alpha)
                           for i in range(moves_no)]

                r = random()

                if r < q0:
                    product = [[i, product[i]] for i in range(moves_no)]
                    best = max(product, key=lambda x: x[1])
                    self.__visited.append(moves[best[0]])
                else:
                    s = sum(product)

                    if s == 0:
                        self.__visited.append(choice(moves))
                    else:
                        product = [product[i] / s for i in range(moves_no)]
                        product = [sum(product[0:i + 1]) for i in range(moves_no)]
                        r = random()
                        i = 0

                        while r > product[i] and i < moves_no:
                            i += 1

                        self.__visited.append(moves[i])

    def __next_moves(self):
        moves = []
        for number in self.__numbers:
            if self.__is_node_visited(number) is False:
                moves.append(number)
        return moves

    def __is_node_visited(self, node):
        return node in self.__visited

    def __replace_graph(self):
        self.__path.append(deepcopy(self.__visited))
        self.__visited = []
        self.__numbers = np.random.permutation(self.__n)
        self.__graph_no += 1

    def fitness(self):
        count = 0
        values = set([item for item in range(1, self.__n + 1)])

        for row in range(0, self.__n):
            if set(self.__path[row]) != values:
                count += 1

        pairs = []

        for j in range(0, self.__n):
            first_column = []
            second_column = []

            for i in range(0, self.__n):
                first_column.append(self.__path[i][j])
                second_column.append(self.__path[i + self.__n][j])
                pairs.append(tuple([self.__path[i][j], self.__path[i + self.__n][j]]))
                
            if set(first_column) != values:
                count += 1

            if set(second_column) != values:
                count += 1

        count += len(pairs) - len(set(pairs))

        return count

    def get_path(self):
        return self.__path

    def get_path_part(self, i):
        return self.__path[i]
