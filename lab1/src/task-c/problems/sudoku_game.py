#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 15:51:14 2020

@author: adrian
"""

import numpy as np


class SudokuGame:

    def __init__(self, attempts, filename):
        self.__attempts = attempts
        self.__board = self.__read_board(filename)

    def solve_problem(self):
        for i in range(self.__attempts):
            possible_solution = self.__solve()
            if self.__is_solution(possible_solution):
                return possible_solution

        return None

    def __solve(self):
        solution = []
        n = len(self.__board)

        for i in range(n):
            row = []
            for j in range(n):
                row.append(np.random.randint(low=1, high=n + 1) if self.__board[i][j] == 0
                           else self.__board[i][j])
            solution.append(row)

        return solution

    @staticmethod
    def __read_board(filename):
        board = []
        file = open(filename, 'r')

        for line in file:
            line_numbers = []
            for n in line.split(' '):
                line_numbers.append(int(n))
            board.append(line_numbers)
        file.close()

        return board

    @staticmethod
    def __is_solution(board):
        numbers = set(range(1, len(board) + 1))

        if (any(set(row) != numbers for row in board) or
                any(set(col) != numbers for col in zip(*board))):
            return False

        return True
