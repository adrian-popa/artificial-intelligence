#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 15:16:13 2020

Develop an application that performs random searches to the following problems.

@author: adrian
"""

import time

from problems.sudoku_game import SudokuGame
from problems.cryptarithmetic_game import CryptarithmeticGame
from problems.geometric_forms import GeometricForms


def show_menu():
    menu = '1. Sudoku game\n'
    menu += '2. Cryptarithmetic game\n'
    menu += '3. Geometric forms\n'
    print(menu)


def read_input():
    problem = input('Choose the problem (1, 2 or 3): ')
    attempts = int(input('Number of attempts: '))
    filename = ''
    if problem == '1' or problem == '2':
        filename = input('Your input file: ')
    return problem, attempts, filename


def search_solution(problem, attempts, filename):
    start_time = time.time()

    if problem == '1':
        print('Sudoku game working...')
        solution = SudokuGame(attempts, filename).solve_problem()
        if solution is None:
            on_retry(problem, filename)
            return
        for line in solution:
            print(line)
    if problem == '2':
        print('Cryptarithmetic game working...')
        solution = CryptarithmeticGame(attempts, filename).solve_problem()
        if solution is None:
            on_retry(problem, filename)
            return
        print(solution)
    if problem == '3':
        print('Geometric forms working...')
        solution = GeometricForms(attempts).solve_problem()
        if solution is None:
            on_retry(problem, filename)
            return
        for line in solution:
            print(line)

    print("\n--- Task took %s seconds to complete ---" % (time.time() - start_time))


def on_retry(problem, filename):
    print("No possible solution found in the given attempts.")
    retry = input('Retry? (y/N): ')
    if retry.upper() == 'Y':
        attempts = int(input('Number of attempts: '))
        search_solution(problem, attempts, filename)


def main():
    show_menu()
    problem, attempts, filename = read_input()
    search_solution(problem, attempts, filename)


main()
