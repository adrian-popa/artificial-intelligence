#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 15:52:53 2020

@author: adrian
"""

import numpy as np


class GeometricForms:

    def __init__(self, attempts):
        self.__attempts = attempts

    def solve_problem(self):
        for i in range(self.__attempts):
            possible_solution, solution = self.__solve()
            if self.__check(possible_solution):
                return solution

        return None

    @staticmethod
    def __solve():
        matrix = np.zeros((5, 6))
        display = np.zeros((5, 6))

        possible_forms = [
            [[0, 0, 0, 0], [1, 1, 1, 1]],
            [[1, 0, 0, 0], [1, 1, 1, 0]],
            [[0, 1, 0, 1], [0, 1, 1, 1]],
            [[0, 1, 1, 1], [0, 0, 0, 1]],
            [[0, 1, 0, 0], [1, 1, 1, 0]]
        ]

        for k in range(0, 5):
            x = np.random.randint(0, 3)
            y = np.random.randint(0, 4)

            for i in range(y, y + 2):
                for j in range(x, x + 4):
                    matrix[i][j] = matrix[i][j] + possible_forms[k][i - y][j - x]
                    display[i][j] = k + 1 if possible_forms[k][i - y][j - x] == 1 else display[i][j]

        return matrix, display

    @staticmethod
    def __check(matrix):
        for i in range(0, 5):
            for j in range(0, 6):
                if matrix[i][j] > 1:
                    return False
        return True
