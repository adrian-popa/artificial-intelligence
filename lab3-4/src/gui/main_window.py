from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QWidget

from gui.evolutionary_algorithm_window import EvolutionaryAlgorithmWindow
from gui.hill_climbing_method_window import HillClimbingMethodWindow
from gui.particle_swarm_optimisation_window import ParticleSwarmOptimisationWindow


class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent, flags=Qt.WindowFlags())

        self.__init_gui()

    def __init_gui(self):
        self.setWindowTitle('Lab3-4')

        self.ea_button = QPushButton('Evolutionary Algorithm', self)
        self.ea_button.clicked.connect(self.__ea_button_clicked)

        self.hcm_button = QPushButton('Hill Climbing Method', self)
        self.hcm_button.clicked.connect(self.__hcm_button_clicked)

        self.pso_button = QPushButton('Particle Swarm Optimisation', self)
        self.pso_button.clicked.connect(self.__pso_button_clicked)

        self.qv_box_layout = QVBoxLayout()
        self.qv_box_layout.setContentsMargins(20, 20, 20, 20)
        self.qv_box_layout.addWidget(self.ea_button, alignment=Qt.Alignment())
        self.qv_box_layout.addWidget(self.hcm_button, alignment=Qt.Alignment())
        self.qv_box_layout.addWidget(self.pso_button, alignment=Qt.Alignment())

        self.setCentralWidget(QWidget(flags=Qt.WindowFlags()))
        self.centralWidget().setLayout(self.qv_box_layout)

    def __ea_button_clicked(self):
        evolutionary_algorithm_window = EvolutionaryAlgorithmWindow(self)
        evolutionary_algorithm_window.show()

    def __hcm_button_clicked(self):
        hill_climbing_method_window = HillClimbingMethodWindow(self)
        hill_climbing_method_window.show()

    def __pso_button_clicked(self):
        particle_swarm_optimisation_window = ParticleSwarmOptimisationWindow(self)
        particle_swarm_optimisation_window.show()
