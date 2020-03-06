#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 3 15:06:37 2020

@author: adrian
"""

import numpy as np
import matplotlib.pyplot as plt


def gen_normal(mu, sigma):
    t = np.random.normal(mu, sigma, 100)
    plt.plot(t, 'bo')
    plt.title('Normal distribution')
    plt.show()


def gen_binomial(n, p):
    t = np.random.binomial(n, p, 100)
    plt.plot(t, 'bo')
    plt.title('Bino distribution')
    plt.show()


def generate(distr, start, end):
    t = np.random.randint(low=start, high=end, size=100)
    plt.plot(t, 'ro')
    plt.title('Generated random numbers')
    plt.show()

    if distr == '1':
        gen_normal(0, 0.05)
    if distr == '2':
        gen_binomial(15, 0.25)


def show_menu():
    menu = '1. Normal distribution\n'
    menu += '2. Binomial distribution\n'
    print(menu)


def read_input():
    distr = input('Choose the distribution (1 or 2): ')
    start = int(input('Start: '))
    end = int(input('End: '))
    return distr, start, end


def main():
    show_menu()
    distr, start, end = read_input()
    generate(distr, start, end)


main()
