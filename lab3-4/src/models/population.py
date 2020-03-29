from random import randint

from models.individual import Individual


class Population:
    def __init__(self, n, population_size, prob_gene, prob_mutation):
        self.__population_size = population_size
        self.__prob_gene = prob_gene
        self.__prob_mutation = prob_mutation
        self.__n = n
        self.__population = self.generate_population()

    def generate_population(self):
        initial_pop = []
        for i in range(self.__population_size):
            individual = Individual(self.__n)
            initial_pop.append(individual)
        return initial_pop[:]

    def get_population(self):
        return self.__population

    def natural_selection(self):
        return sorted(self.__population, key=lambda x: x.fitness())[:self.__population_size]

    def iteration(self):
        i1 = randint(0, self.__population_size - 1)
        i2 = randint(0, self.__population_size - 1)
        if i1 != i2:
            child1, child2 = self.__population[i1].crossover(self.__population[i2], self.__prob_gene)
            child1.mutate(self.__prob_mutation)
            child2.mutate(self.__prob_mutation)
            self.__population.append(child1)
            self.__population.append(child2)
        self.__population = self.natural_selection()
