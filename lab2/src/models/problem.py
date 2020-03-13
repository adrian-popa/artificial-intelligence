# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 14:33:14 2020
@author: adrian
"""

from numpy import double


class Problem:

    @staticmethod
    def expand(state):
        if not state:
            raise RuntimeError('The initial state is not defined, please set the size of the matrix first.')

        for line in state.get_values():
            if 0 in line:
                return state.get_next_values()

        return []

    @staticmethod
    def get_final(state):
        if not state:
            raise RuntimeError('The initial state is not defined, please set the size of the matrix first.')

        for line in state.get_values():
            if sum(line) != 1:
                return False

        return True

    @staticmethod
    def heuristics(state):
        if not state.is_valid():
            return -double('inf')

        values = state.get_values()

        cost = 0

        for i in range(len(values)):
            for j in range(len(values)):
                if values[i][j] == 1:
                    cost += 1

        return cost
