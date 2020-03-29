from statistics import stdev, mean

from PyQt5.QtCore import QThread, pyqtSignal

from models.hill_climbing_method import HillClimbingMethod


class HillClimbingMethodService(QThread):
    signal = pyqtSignal('PyQt_PyObject')

    def __init__(self, filename):
        QThread.__init__(self)
        self.__filename = filename

    def run(self):
        n, runs = self.__read_hcm_stats(self.__filename)
        best_solutions = []
        algorithm = HillClimbingMethod()
        for i in range(runs):
            result = algorithm.run(n)
            best_solutions.append(result[1])
            if i % 100 == 0:
                self.signal.emit([min(best_solutions), i])
        std_fit = stdev(best_solutions)
        mean_fit = mean(best_solutions)
        self.signal.emit([std_fit, mean_fit, best_solutions])

    @staticmethod
    def __read_hcm_stats(filename):
        with open(filename, 'r') as fin:
            n = int(fin.readline())
            runs = int(fin.readline())
            return n, runs
