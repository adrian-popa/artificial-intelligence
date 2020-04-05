from controllers.controller import Controller
from models.problem import Problem
from ui.ui import UI


def main():
    problem = Problem('ant.in')
    controller = Controller('ant-params.in', problem)
    ui = UI(controller)
    ui.run()


main()
