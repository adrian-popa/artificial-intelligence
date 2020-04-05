class Problem:

    def __init__(self, filename):
        self.__filename = filename
        self.__n = self.__load_problem()

    def __load_problem(self):
        file = open(self.__filename, 'r')

        n = int(file.readline())

        file.close()

        return n

    def get_size(self):
        return self.__n
