from statistics import stdev, mean

from PyQt5.QtCore import pyqtSignal, QThread

from models.particle_swarm_optimisation import ParticleSwarmOptimisation


class ParticleSwarmOptimisationService(QThread):
    signal = pyqtSignal('PyQt_PyObject')

    def __init__(self, filename):
        QThread.__init__(self)
        self.__filename = filename

    def run(self):
        n, particle_size, w, c1, c2, v_min, v_max, neighbourhood_size, iterations, runs = self.__read_pso_stats(
            self.__filename)
        best_solutions = []
        algorithm = ParticleSwarmOptimisation()
        for i in range(runs):
            result = algorithm.run(n, particle_size, w, c1, c2, v_min, v_max, neighbourhood_size, iterations)
            best_solutions.append(result[1])
            if i % 100 == 0:
                self.signal.emit([min(best_solutions), i])
        std_fit = stdev(best_solutions)
        mean_fit = mean(best_solutions)
        self.signal.emit([std_fit, mean_fit, best_solutions])

    @staticmethod
    def __read_pso_stats(filename):
        with open(filename, 'r') as fin:
            n = int(fin.readline())
            particle_size = int(fin.readline())
            w = float(fin.readline())
            c1 = float(fin.readline())
            c2 = float(fin.readline())
            v_min = int(fin.readline())
            v_max = int(fin.readline())
            neigh_size = int(fin.readline())
            iterations = int(fin.readline())
            runs = int(fin.readline())
            return n, particle_size, w, c1, c2, v_min, v_max, iterations, neigh_size, runs
