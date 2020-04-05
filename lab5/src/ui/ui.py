import time


class UI:

    def __init__(self, controller):
        self.__controller = controller

    def run(self):
        problem = self.__controller.get_problem()

        trace = [[[1 for _ in range(problem.get_size())] for _ in range(problem.get_size())]
                 for _ in range(2 * problem.get_size())]

        start_time = time.time()

        print('ACO working...')

        best_ant = None

        for i in range(self.__controller.get_no_epoch()):
            solution = self.__controller.epoch(trace)

            if best_ant is None:
                best_ant = solution

            if solution.fitness() < best_ant.fitness():
                best_ant = solution

        print("Best solution fitness:", best_ant.fitness())

        print("Final solution:")

        for line in best_ant.get_path():
            print(line)

        print('\n--- Task took %s seconds to complete ---' % (time.time() - start_time))
