from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QPushButton, QHBoxLayout, QLabel, QLineEdit, QVBoxLayout, QWidget
from matplotlib import pyplot

from models.hill_climbing_method import HillClimbingMethodThreaded
from services.hill_climbing_method_service import HillClimbingMethodService


class HillClimbingMethodWindow(QMainWindow):

    def __init__(self, parent=None):
        super(HillClimbingMethodWindow, self).__init__(parent, flags=Qt.WindowFlags())

        self.__init_gui()
        self.__algorithm = HillClimbingMethodThreaded(1)
        self.__algorithm.signal.connect(self.status)
        self.__thread = HillClimbingMethodService('hcm.in')
        self.__thread.signal.connect(self.received)

    def __init_gui(self):
        self.setWindowTitle('Hill Climbing Method')

        individual_size_box = QHBoxLayout()
        individual_size_label = QLabel('Individual size:')
        individual_size_label.setMinimumWidth(150)
        self.individual_size_input = QLineEdit()
        individual_size_box.addWidget(individual_size_label, alignment=Qt.Alignment())
        individual_size_box.addWidget(self.individual_size_input, alignment=Qt.Alignment())

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
        self.qv_box_layout.addWidget(self.solution_label, alignment=Qt.Alignment())
        self.qv_box_layout.addWidget(self.statistics_label, alignment=Qt.Alignment())
        self.qv_box_layout.addLayout(self.solutions_buttons_box)
        self.qv_box_layout.addLayout(self.statistics_buttons_box)
        self.setCentralWidget(QWidget(flags=Qt.WindowFlags()))
        self.centralWidget().setLayout(self.qv_box_layout)

    def __solution_button_clicked(self):
        self.__algorithm = HillClimbingMethodThreaded(int(self.individual_size_input.text()))
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
            print('[HCM] Step: ' + str(data[1]) + ', best fitness so far: ' + str(data[0]))

    def received(self, data):
        if len(data) == 3:
            self.statistics_button.setEnabled(True)
            self.terminate_statistics_button.setEnabled(False)
            self.statistics_label.setText('Std dev: ' + str(data[0]) + '\nMean:' + str(data[1]))
            pyplot.plot(data[2])
            pyplot.show()
        else:
            print('[HCM] Step: ' + str(data[1]) + ', best fitness so far: ' + str(data[0]))
