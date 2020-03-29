from PyQt5.QtCore import QThread, pyqtSignal

from models.particle_swarm_optimisation_population import ParticleSwarmOptimisationPopulation


class ParticleSwarmOptimisation:

    @staticmethod
    def run(n, particle_size, w, c1, c2, v_min, v_max, neighbourhood_size, iterations):
        p = ParticleSwarmOptimisationPopulation(n, particle_size, v_min, v_max)

        neighbours = p.select_neighbours(neighbourhood_size)

        for i in range(iterations):
            p.iteration(neighbours, c1, c2, w / (i + 1))

        best = p.get_best()
        return best, best.fitness()


class ParticleSwarmOptimisationThreaded(QThread):
    signal = pyqtSignal('PyQt_PyObject')

    def __init__(self, n, particle_size, w, c1, c2, v_min, v_max, neighbourhood_size, iterations):
        QThread.__init__(self)
        self.__n = n
        self.__particle_size = particle_size
        self.__w = w
        self.__c1 = c1
        self.__c2 = c2
        self.__v_min = v_min
        self.__v_max = v_max
        self.__neighbourhood_size = neighbourhood_size
        self.__iterations = iterations

    def run(self):
        best_solutions = []
        p = ParticleSwarmOptimisationPopulation(self.__n, self.__particle_size, self.__v_min, self.__v_max)

        neighbours = p.select_neighbours(self.__neighbourhood_size)

        for i in range(self.__iterations):
            p.iteration(neighbours, self.__c1, self.__c2, self.__w / (i + 1))
            best_solutions.append(p.get_best().fitness())
            if i % 10 == 0:
                self.signal.emit([min(best_solutions), i])
        best = p.get_best()
        self.signal.emit([best, best.fitness(), 'done'])
