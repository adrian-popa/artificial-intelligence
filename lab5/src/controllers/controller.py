from models.ant import Ant


class Controller:

    def __init__(self, filename, problem):
        self.__filename = filename
        self.__problem = problem
        self.__noEpoch = 0
        self.__noAnts = 0
        self.__alpha = 0.0
        self.__beta = 0.0
        self.__rho = 0.0
        self.__q0 = 0.0

        self.__load_params()

    def __load_params(self):
        file = open(self.__filename, 'r')
        lines = file.read().splitlines()

        self.__noEpoch = int(lines[0])
        self.__noAnts = int(lines[1])
        self.__alpha = float(lines[2])
        self.__beta = float(lines[3])
        self.__rho = float(lines[4])
        self.__q0 = float(lines[5])

        file.close()

    def get_no_epoch(self):
        return self.__noEpoch

    def epoch(self, trace):
        ant_set = [Ant(self.__problem) for _ in range(self.__noAnts)]

        for i in range(2 * self.__problem.get_size() * self.__problem.get_size()):
            for ant in ant_set:
                ant.update(trace, self.__alpha, self.__beta, self.__q0)

        d_trace = [1.0 / ant_set[i].fitness() for i in range(len(ant_set))]

        for i in range(2 * self.__problem.get_size()):
            for j in range(self.__problem.get_size()):
                for k in range(self.__problem.get_size()):
                    trace[i][j][k] = (1 - self.__rho) * trace[i][j][k]

        for i in range(len(ant_set)):
            for j in range(2 * self.__problem.get_size()):
                for k in range(self.__problem.get_size() - 1):
                    x = ant_set[i].get_path_part(j)[k]
                    y = ant_set[i].get_path_part(j)[k + 1]
                    trace[j][x][y] = trace[j][x][y] + d_trace[i]

        f = [[ant_set[i].fitness(), i] for i in range(len(ant_set))]
        f = min(f)

        return ant_set[f[1]]

    def get_problem(self):
        return self.__problem
