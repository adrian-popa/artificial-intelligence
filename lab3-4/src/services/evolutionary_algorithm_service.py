from statistics import stdev, mean

from PyQt5.QtCore import QThread, pyqtSignal

from models.evolutionary_algorithm import EvolutionaryAlgorithm


class EvolutionaryAlgorithmService(QThread):
    signal = pyqtSignal('PyQt_PyObject')

    def __init__(self, filename):
        QThread.__init__(self)
        self.__filename = filename

    def run(self):
        n, population_size, runs, generations, cross_prob, mutation_prob = self.__read_ea_stats(self.__filename)
        best_solutions = []
        for i in range(runs):
            result = EvolutionaryAlgorithm.run(generations, n, population_size, cross_prob, mutation_prob)
            best_solutions.append(result[1])
            if i % 100 == 0:
                self.signal.emit([min(best_solutions), i])
        std_fit = stdev(best_solutions)
        mean_fit = mean(best_solutions)
        self.signal.emit([std_fit, mean_fit, best_solutions])

    @staticmethod
    def __read_ea_stats(filename):
        with open(filename, 'r') as fin:
            n = int(fin.readline())
            pop_size = int(fin.readline())
            runs = int(fin.readline())
            generations = int(fin.readline())
            cross_prob = float(fin.readline())
            mutation_prob = float(fin.readline())
            return n, pop_size, runs, generations, cross_prob, mutation_prob
