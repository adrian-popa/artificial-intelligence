# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 14:32:46 2020
@author: adrian
"""

from copy import deepcopy
from queue import PriorityQueue

from models.problem import Problem
from repositories.state import State


class Controller:

    def __init__(self):
        self.__instance = None
        self.__root = None
        self.__problem = Problem()

    def init_state(self, n):
        self.__instance = State(n)
        self.__root = State(n)

    def greedy(self):
        visited = []
        to_visit = [deepcopy(self.__root)]

        while len(to_visit) > 0:
            if len(to_visit) == 0:
                return None

            current_node = to_visit.pop(0)
            if current_node not in visited:
                visited.append(current_node)

            if Problem.get_final(current_node):
                return current_node

            for expanded in Problem.expand(current_node):
                if expanded not in visited:
                    if Problem.get_final(expanded):
                        return expanded
                    visited.append(expanded)
                    to_visit = [expanded] + to_visit

            to_visit = sorted(to_visit, key=lambda state: Problem.heuristics(state), reverse=True)

        return None

    def dfs(self):
        visited = []
        to_visit = [deepcopy(self.__root)]
        final = []

        while len(to_visit) > 0:
            if len(to_visit) == 0:
                return None

            current_node = to_visit.pop()

            if current_node not in visited:
                visited.append(current_node)

            if Problem.get_final(current_node):
                final.append(current_node)

            for expanded in Problem.expand(current_node):
                if expanded not in visited:
                    visited.append(expanded)
                    to_visit += [expanded]

        return final

    # TODO: Implement PriorityQueue DFS method
    # def dfs_pq(self):
    #     visited = []
    #     final = []
    #
    #     fringe = PriorityQueue()
    #     fringe.put((0, deepcopy(self.__root), final, visited))
    #
    #     while not fringe.empty():
    #         depth, current_node, final, visited = fringe.get()
    #
    #         if current_node == self.__problem.get_final(current_node):
    #             return final + [current_node]
    #
    #         visited += [current_node]
    #
    #         child_nodes = Problem.expand(current_node)
    #
    #         for node in child_nodes:
    #             if node not in visited:
    #                 if node == self.__problem.get_final:
    #                     return final + [node]
    #                 depth_of_node = len(final)
    #                 fringe.put((-depth_of_node, node, final + [node], visited + [node]))
    #
    #     return final
