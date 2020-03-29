import copy

from PyQt5.QtCore import QThread, pyqtSignal

from models.individual import Individual


class HillClimbingMethod:

    @staticmethod
    def run(n):
        current_node = Individual(n)

        while current_node.fitness() > 0:
            neighbours = current_node.get_neighbours()
            neighbours.sort(key=lambda b: b.fitness())
            best_neighbour = neighbours[0]

            if best_neighbour.fitness() < current_node.fitness():
                current_node = copy.deepcopy(best_neighbour)
            else:
                return current_node, current_node.fitness()

        return current_node, current_node.fitness()


class HillClimbingMethodThreaded(QThread):
    signal = pyqtSignal('PyQt_PyObject')

    def __init__(self, n):
        QThread.__init__(self)
        self.__n = n

    def run(self):
        current_node = Individual(self.__n)

        while current_node.fitness() > 0:
            neighbours = current_node.get_neighbours()
            neighbours.sort(key=lambda b: b.fitness())
            best_neighbour = neighbours[0]

            if best_neighbour.fitness() < current_node.fitness():
                current_node = copy.deepcopy(best_neighbour)
            else:
                self.signal.emit([current_node, current_node.fitness(), 'done'])
                return

        self.signal.emit([current_node, current_node.fitness(), 'done'])
