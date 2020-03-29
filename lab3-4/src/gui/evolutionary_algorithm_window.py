from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QPushButton, QHBoxLayout, QLabel, QLineEdit, QVBoxLayout, QWidget
from matplotlib import pyplot

from models.evolutionary_algorithm import EvolutionaryAlgorithmThreaded
from services.evolutionary_algorithm_service import EvolutionaryAlgorithmService


class EvolutionaryAlgorithmWindow(QMainWindow):

    def __init__(self, parent=None):
        super(EvolutionaryAlgorithmWindow, self).__init__(parent, flags=Qt.WindowFlags())

        self.__init_gui()
        self.__algorithm = EvolutionaryAlgorithmThreaded(1, 1, 1, 1, 1)
        self.__algorithm.signal.connect(self.status)
        self.__thread = EvolutionaryAlgorithmService('ea.in')
        self.__thread.signal.connect(self.received)

    def __init_gui(self):
        self.setWindowTitle('Evolutionary Algorithm')

        individual_size_box = QHBoxLayout()
        individual_size_label = QLabel('Individual size:')
        individual_size_label.setMinimumWidth(150)
        self.individual_size_input = QLineEdit()
        individual_size_box.addWidget(individual_size_label, alignment=Qt.Alignment())
        individual_size_box.addWidget(self.individual_size_input, alignment=Qt.Alignment())

        population_size_box = QHBoxLayout()
        population_size_label = QLabel('Population size:')
        population_size_label.setMinimumWidth(150)
        self.population_size_input = QLineEdit()
        population_size_box.addWidget(population_size_label, alignment=Qt.Alignment())
        population_size_box.addWidget(self.population_size_input, alignment=Qt.Alignment())

        mutations_probability_box = QHBoxLayout()
        mutations_probability_label = QLabel('Mutations probability:')
        mutations_probability_label.setMinimumWidth(150)
        self.mutations_probability_input = QLineEdit()
        mutations_probability_box.addWidget(mutations_probability_label, alignment=Qt.Alignment())
        mutations_probability_box.addWidget(self.mutations_probability_input, alignment=Qt.Alignment())

        crossover_probability_box = QHBoxLayout()
        crossover_probability_label = QLabel('Crossover probability:')
        crossover_probability_label.setMinimumWidth(150)
        self.crossover_probability_input = QLineEdit()
        crossover_probability_box.addWidget(crossover_probability_label, alignment=Qt.Alignment())
        crossover_probability_box.addWidget(self.crossover_probability_input, alignment=Qt.Alignment())

        generations_number_box = QHBoxLayout()
        generations_number_label = QLabel('Number of generations:')
        generations_number_label.setMinimumWidth(150)
        self.generations_number_input = QLineEdit()
        generations_number_box.addWidget(generations_number_label, alignment=Qt.Alignment())
        generations_number_box.addWidget(self.generations_number_input, alignment=Qt.Alignment())

        self.solution_label = QLabel()

        self.solution_button = QPushButton('Solution', self)
        self.solution_button.clicked.connect(self.__solution_button_clicked)

        self.terminate_solution_button = QPushButton('Terminate solution', self)
        self.terminate_solution_button.clicked.connect(self.__terminate_solution)
        self.terminate_solution_button.setEnabled(False)

        self.statistics_label = QLabel()

        self.statistics_button = QPushButton('Statistics', self)
        self.statistics_button.clicked.connect(self.__statistics_button_clicked)

        self.terminate_statistics_button = QPushButton('Terminate statistics', self)
        self.terminate_statistics_button.clicked.connect(self.__terminate_statistics)
        self.terminate_statistics_button.setEnabled(False)

        self.solutions_buttons_box = QHBoxLayout()
        self.solutions_buttons_box.addWidget(self.solution_button, alignment=Qt.Alignment())
        self.solutions_buttons_box.addWidget(self.terminate_solution_button, alignment=Qt.Alignment())

        self.statistics_buttons_box = QHBoxLayout()
        self.statistics_buttons_box.addWidget(self.statistics_button, alignment=Qt.Alignment())
        self.statistics_buttons_box.addWidget(self.terminate_statistics_button, alignment=Qt.Alignment())

        self.qv_box_layout = QVBoxLayout()
        self.qv_box_layout.addLayout(individual_size_box)
        self.qv_box_layout.addLayout(population_size_box)
        self.qv_box_layout.addLayout(mutations_probability_box)
        self.qv_box_layout.addLayout(crossover_probability_box)
        self.qv_box_layout.addLayout(generations_number_box)
        self.qv_box_layout.addWidget(self.solution_label, alignment=Qt.Alignment())
        self.qv_box_layout.addWidget(self.statistics_label, alignment=Qt.Alignment())
        self.qv_box_layout.addLayout(self.solutions_buttons_box)
        self.qv_box_layout.addLayout(self.statistics_buttons_box)
        self.setCentralWidget(QWidget(flags=Qt.WindowFlags()))
        self.centralWidget().setLayout(self.qv_box_layout)

    def __solution_button_clicked(self):
        self.__algorithm = EvolutionaryAlgorithmThreaded(
            int(self.generations_number_input.text()), int(self.individual_size_input.text()),
            int(self.population_size_input.text()),
            float(self.crossover_probability_input.text()),
            float(self.mutations_probability_input.text())
        )
        self.__algorithm.signal.connect(self.status)
        self.__algorithm.start()
        self.terminate_solution_button.setEnabled(True)
        self.solution_button.setEnabled(False)

    def __terminate_solution(self):
        self.__algorithm.terminate()
        self.terminate_solution_button.setEnabled(False)
        self.solution_button.setEnabled(True)

    def __statistics_button_clicked(self):
        self.statistics_button.setEnabled(False)
        self.terminate_statistics_button.setEnabled(True)
        self.__thread.start()

    def __terminate_statistics(self):
        self.__thread.terminate()
        self.statistics_button.setEnabled(True)
        self.terminate_statistics_button.setEnabled(False)

    def status(self, data):
        if len(data) == 3:
            self.solution_button.setEnabled(True)
            self.terminate_solution_button.setEnabled(False)
            self.solution_label.setText('Solution:\n' + str(data[0]) + '\nFitness:' + str(data[1]))
        else:
            print('[EA] Step: ' + str(data[1]) + ', best fitness so far: ' + str(data[0]))

    def received(self, data):
        if len(data) == 3:
            self.statistics_button.setEnabled(True)
            self.terminate_statistics_button.setEnabled(False)
            self.statistics_label.setText('Std dev: ' + str(data[0]) + '\nMean:' + str(data[1]))
            pyplot.plot(data[2])
            pyplot.show()
        else:
            print('[EA] Step: ' + str(data[1]) + ', best fitness so far: ' + str(data[0]))
