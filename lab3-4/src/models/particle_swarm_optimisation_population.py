from math import exp
from random import random

import numpy as np

from models.particle import Particle


class ParticleSwarmOptimisationPopulation:
    def __init__(self, n, particle_size, v_min, v_max):
        self.__n = n
        self.__particle_size = particle_size
        self.__v_min = v_min
        self.__v_max = v_max
        self.__population = self.generate_population()

    def generate_population(self):
        initial_population = []
        for i in range(self.__n):
            particle = Particle(self.__particle_size, self.__v_min, self.__v_max)
            initial_population.append(particle)
        return initial_population[:]

    def get_best(self):
        self.__population.sort(key=lambda x: x.fitness())
        return self.__population[0]

    def select_neighbours(self, size):
        neighbours = []
        for p in self.__population:
            neighbours += p.get_neighbours(size)
        return neighbours

    def iteration(self, neighbours, c1, c2, w):
        best_neighbours = []
        for i in range(len(self.__population)):
            best_neighbours.append(neighbours[0])
            for j in range(1, len(neighbours)):
                if best_neighbours[i].fitness() < neighbours[j].fitness():
                    best_neighbours[i] = neighbours[j]

        for i in range(len(self.__population)):
            for j in range(len(self.__population[0].get_velocity())):
                new_velocity_s = w * self.__population[i].get_velocity()[j][0] + \
                    c1 * random() * (self.__manhattan_distance(
                        best_neighbours[i].get_line_from_s(j), self.__population[i].get_line_from_s(j))) + \
                    c2 * random() * (
                        self.__manhattan_distance(
                            self.__population[i].get_best_position().get_line_from_s(j),
                            self.__population[i].get_line_from_s(j)))
                new_velocity_t = w * self.__population[i].get_velocity()[j][1] + \
                    c1 * random() * (self.__manhattan_distance(
                        best_neighbours[i].get_line_from_t(j), self.__population[i].get_line_from_t(j))) + \
                    c2 * random() * (
                        self.__manhattan_distance(
                            self.__population[i].get_best_position().get_line_from_t(j),
                            self.__population[i].get_line_from_t(j)))
                self.__population[i].get_velocity()[j][0] = new_velocity_s
                self.__population[i].get_velocity()[j][1] = new_velocity_t

        for i in range(len(self.__population)):
            for j in range(len(self.__population[0].get_velocity())):
                if random() < self.__sigmoid_function(self.__population[i].get_velocity()[j][0]):
                    self.__population[i].set_line_from_s(j, best_neighbours[i].get_line_from_s(j))
                if random() < self.__sigmoid_function(self.__population[i].get_velocity()[j][1]):
                    self.__population[i].set_line_from_t(j, best_neighbours[i].get_line_from_t(j))

    @staticmethod
    def __sigmoid_function(v):
        return exp(-np.logaddexp(0, -v))

    @staticmethod
    def __manhattan_distance(line1, line2):
        dist = 0
        for i in range(len(line1)):
            dist += line1[i] - line2[i]
        return dist
