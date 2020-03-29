from PyQt5.QtCore import pyqtSignal, QThread

from models.population import Population


class EvolutionaryAlgorithm:

    @staticmethod
    def run(generations, n, pop_size, cross_prob, mutation_prob):
        p = Population(n, pop_size, cross_prob, mutation_prob)
        for i in range(generations):
            p.iteration()
        return p.get_population()[0], p.get_population()[0].fitness()


class EvolutionaryAlgorithmThreaded(QThread):
    signal = pyqtSignal('PyQt_PyObject')

    def __init__(self, generations, n, pop_size, cross_prob, mutation_prob):
        QThread.__init__(self)
        self.__generations = generations
        self.__n = n
        self.__pop_size = pop_size
        self.__cross_prob = cross_prob
        self.__mutation_prob = mutation_prob

    def run(self):
        best = []
        p = Population(self.__n, self.__pop_size, self.__cross_prob, self.__mutation_prob)
        for i in range(self.__generations):
            p.iteration()
            best.append(p.get_population()[0].fitness())
            if i % 10 == 0:
                self.signal.emit([min(best), i])

        self.signal.emit([p.get_population()[0], p.get_population()[0].fitness(), 'done'])
