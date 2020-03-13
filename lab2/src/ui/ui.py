# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 14:32:31 2020
@author: adrian
"""

from time import time


class UI:

    def __init__(self, controller):
        self.__controller = controller

    @staticmethod
    def print_menu():
        s = '0 - exit\n'
        s += '1 - read the size of the matrix\n'
        s += '2 - find the solution with Greedy\n'
        s += '3 - find the solutions with DFS\n'
        print(s)

    def find_path_greedy(self):
        start_clock = time()

        solution = self.__controller.greedy()
        if solution is None:
            print("No solution has been found.")
            return

        print(solution)
        print('Greedy execution time: ' + str(time() - start_clock) + ' seconds')

    def find_path_dfs(self):
        start_clock = time()

        solutions = self.__controller.dfs()
        if len(solutions) == 0:
            print("No solutions have been found.")
            return

        for solution in solutions:
            print(solution)
        print('DFS execution time: ' + str(time() - start_clock) + ' seconds')

    def run(self):
        self.print_menu()

        keep_alive = True
        while keep_alive:
            try:
                command = int(input('>> '))
                if command == 0:
                    keep_alive = False
                elif command == 1:
                    n = int(input('n: '))
                    self.__controller.init_state(n)
                elif command == 2:
                    self.find_path_greedy()
                elif command == 3:
                    self.find_path_dfs()
                else:
                    print('Invalid command')
            except RuntimeError as e:
                print(e)
