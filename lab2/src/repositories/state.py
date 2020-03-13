# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 14:32:57 2020
@author: adrian
"""

from copy import deepcopy


class State:
    """
    holds a the state of the Matrix
    """

    def __init__(self, n):
        self.__values = [[0 for _ in range(n)] for _ in range(n)]
        self.__n = n

    def get_values(self):
        return self.__values

    def set_values(self, values):
        self.__values = values

    def get_next_values(self):
        next_values = []

        for i in range(self.__n):
            for j in range(self.__n):
                if self.__values[i][j] != 1 and self.can_mark_spot(i, j):
                    new_matrix = deepcopy(self.__values)
                    new_matrix[i][j] = 1
                    new_state = State(self.__n)
                    new_state.set_values(new_matrix)
                    next_values.append(new_state)

        return next_values

    def is_valid(self):
        for i in range(self.__n):
            for j in range(self.__n):
                if self.__values[i][j] == 1 and not self.can_mark_spot(i, j):
                    return False

        return True

    def can_mark_spot(self, row, col):
        for i in range(self.__n):
            for j in range(self.__n):
                if self.__values[i][j] == 1:
                    if (i == row or j == col or
                            abs(i - row) - abs(j - col) == 0):
                        return False

        return True

    def __eq__(self, other):
        for i in range(self.__n):
            for j in range(self.__n):
                if self.__values[i][j] != other.get_values()[i][j]:
                    return False

        return True

    def __str__(self):
        string = ''

        for row in self.__values:
            string += str(row) + '\n'

        return string
