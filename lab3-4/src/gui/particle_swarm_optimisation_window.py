from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QHBoxLayout, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget
from matplotlib import pyplot

from models.particle_swarm_optimisation import ParticleSwarmOptimisationThreaded
from services.particle_swarm_optimisation_service import ParticleSwarmOptimisationService


class ParticleSwarmOptimisationWindow(QMainWindow):

    def __init__(self, parent=None):
        super(ParticleSwarmOptimisationWindow, self).__init__(parent, flags=Qt.WindowFlags())

        self.__init_gui()
        self.__algorithm = ParticleSwarmOptimisationThreaded(1, 1, 1, 1, 1, 1, 1, 1, 1)
        self.__algorithm.signal.connect(self.status)
        self.__thread = ParticleSwarmOptimisationService('pso.in')
        self.__thread.signal.connect(self.received)

    def __init_gui(self):
        self.setWindowTitle('Particle Swarm Optimisation')

        individual_size_box = QHBoxLayout()
        individual_size_label = QLabel('Individual size:')
        individual_size_label.setMinimumWidth(150)
        self.individual_size_input = QLineEdit()
        individual_size_box.addWidget(individual_size_label, alignment=Qt.Alignment())
        individual_size_box.addWidget(self.individual_size_input, alignment=Qt.Alignment())

        particles_number_box = QHBoxLayout()
        particles_number_label = QLabel('Number of particles (n):')
        particles_number_label.setMinimumWidth(150)
        self.particles_number_input = QLineEdit()
        particles_number_box.addWidget(particles_number_label, alignment=Qt.Alignment())
        particles_number_box.addWidget(self.particles_number_input, alignment=Qt.Alignment())

        inertia_coefficient_box = QHBoxLayout()
        inertia_coefficient_label = QLabel('w:')
        inertia_coefficient_label.setMinimumWidth(150)
        self.inertia_coefficient_input = QLineEdit()
        inertia_coefficient_box.addWidget(inertia_coefficient_label, alignment=Qt.Alignment())
        inertia_coefficient_box.addWidget(self.inertia_coefficient_input, alignment=Qt.Alignment())

        cognitive_coefficient_box = QHBoxLayout()
        cognitive_coefficient_label = QLabel('c1:')
        cognitive_coefficient_label.setMinimumWidth(150)
        self.cognitive_coefficient_input = QLineEdit()
        cognitive_coefficient_box.addWidget(cognitive_coefficient_label, alignment=Qt.Alignment())
        cognitive_coefficient_box.addWidget(self.cognitive_coefficient_input, alignment=Qt.Alignment())

        social_learn_box = QHBoxLayout()
        social_learn_label = QLabel('c2:')
        social_learn_label.setMinimumWidth(150)
        self.social_learn_input = QLineEdit()
        social_learn_box.addWidget(social_learn_label, alignment=Qt.Alignment())
        social_learn_box.addWidget(self.social_learn_input, alignment=Qt.Alignment())

        v_min_box = QHBoxLayout()
        v_min_label = QLabel('vMin:')
        v_min_label.setMinimumWidth(150)
        self.v_min_input = QLineEdit()
        v_min_box.addWidget(v_min_label, alignment=Qt.Alignment())
        v_min_box.addWidget(self.v_min_input, alignment=Qt.Alignment())

        v_max_box = QHBoxLayout()
        v_max_label = QLabel('vMax:')
        v_max_label.setMinimumWidth(150)
        self.v_max_input = QLineEdit()
        v_max_box.addWidget(v_max_label, alignment=Qt.Alignment())
        v_max_box.addWidget(self.v_max_input, alignment=Qt.Alignment())

        neighbourhood_size_box = QHBoxLayout()
        neighbourhood_size_label = QLabel('Neighbourhood size:')
        neighbourhood_size_label.setMinimumWidth(150)
        self.neighbourhood_size_input = QLineEdit()
        neighbourhood_size_box.addWidget(neighbourhood_size_label, alignment=Qt.Alignment())
        neighbourhood_size_box.addWidget(self.neighbourhood_size_input, alignment=Qt.Alignment())

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
        self.qv_box_layout.addLayout(particles_number_box)
        self.qv_box_layout.addLayout(inertia_coefficient_box)
        self.qv_box_layout.addLayout(cognitive_coefficient_box)
        self.qv_box_layout.addLayout(social_learn_box)
        self.qv_box_layout.addLayout(v_min_box)
        self.qv_box_layout.addLayout(v_max_box)
        self.qv_box_layout.addLayout(neighbourhood_size_box)
        self.qv_box_layout.addLayout(generations_number_box)
        self.qv_box_layout.addWidget(self.solution_label, alignment=Qt.Alignment())
        self.qv_box_layout.addWidget(self.statistics_label, alignment=Qt.Alignment())
        self.qv_box_layout.addLayout(self.solutions_buttons_box)
        self.qv_box_layout.addLayout(self.statistics_buttons_box)
        self.setCentralWidget(QWidget(flags=Qt.WindowFlags()))
        self.centralWidget().setLayout(self.qv_box_layout)

    def __solution_button_clicked(self):
        self.__algorithm = ParticleSwarmOptimisationThreaded(
            int(self.individual_size_input.text()),
            int(self.particles_number_input.text()),
            float(self.inertia_coefficient_input.text()),
            float(self.cognitive_coefficient_input.text()),
            float(self.social_learn_input.text()),
            int(self.v_min_input.text()),
            int(self.v_max_input.text()),
            int(self.neighbourhood_size_input.text()),
            int(self.generations_number_input.text())
        )
        self.__algorithm.signal.connect(self.status)
        self.__algorithm.start()
        self.solution_button.setEnabled(False)
        self.terminate_solution_button.setEnabled(True)

    def __terminate_solution(self):
        self.__algorithm.terminate()
        self.solution_button.setEnabled(True)
        self.terminate_solution_button.setEnabled(False)

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
            print('[PSO] Step: ' + str(data[1]) + ', best fitness so far: ' + str(data[0]))

    def received(self, data):
        if len(data) == 3:
            self.statistics_button.setEnabled(True)
            self.terminate_statistics_button.setEnabled(False)
            self.statistics_label.setText('Std dev: ' + str(data[0]) + '\nMean:' + str(data[1]))
            pyplot.plot(data[2])
            pyplot.show()
        else:
            print('[PSO] Step: ' + str(data[1]) + ', best fitness so far: ' + str(data[0]))
