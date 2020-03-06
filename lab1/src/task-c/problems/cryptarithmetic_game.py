#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 15:51:30 2020

@author: adrian
"""

import numpy as np
import itertools


class CryptarithmeticGame:

    def __init__(self, attempts, filename):
        self.__attempts = attempts
        (self.__first_word, self.__operand, self.__second_word,
         self.__result_word, self.__letters) = self.__read_words(filename)

    def solve_problem(self):
        for i in range(self.__attempts):
            self.__solve()
            if self.__found_solution():
                return self.__to_hexa(self.__letters)

        return None

    def __solve(self):
        for letter in self.__letters.keys():
            self.__letters[letter] = np.random.randint(low=0, high=16)

    def __found_solution(self):
        if (self.__letters[self.__first_word[0]] == 0 or self.__letters[self.__second_word[0]] == 0 or
                self.__letters[self.__result_word[0]]) == 0:
            return False

        first_word = self.__map_word(self.__letters, self.__first_word)
        second_word = self.__map_word(self.__letters, self.__second_word)
        result_word = self.__map_word(self.__letters, self.__result_word)

        if self.__operand == '+':
            return (first_word + second_word) == result_word
        elif self.__operand == '-':
            return (first_word - second_word) == result_word

    @staticmethod
    def __read_words(filename):
        file = open(filename, 'r')
        lines = file.read().splitlines()

        first_word = lines[0]
        operand = lines[1]
        second_word = lines[2]
        result_word = lines[3]

        letters = {}
        for letter in itertools.chain(first_word, second_word, result_word):
            letters[letter] = -1

        file.close()

        return first_word, operand, second_word, result_word, letters

    @staticmethod
    def __map_word(letters, word):
        reverse = word[::-1]
        value = 0
        hexa = 1

        for letter in reverse:
            value += letters[letter] * hexa
            hexa *= 16

        return value

    @staticmethod
    def __to_hexa(letters):
        hexa = {
            0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7',
            8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'
        }

        for letter in letters.keys():
            letters[letter] = hexa[letters[letter]]

        return letters
