class Question:
    """
    A Question is used to partition a dataset.
    This class just records a 'column number' (e.g., 1 for Left-Weight) and a 'column value' (e.g., 3).
    The 'match' method is used to compare the feature value in an example to the feature value stored in the question.
    """

    def __init__(self, header, column, value):
        self.__header = header
        self.__column = column
        self.__value = value

    @staticmethod
    def is_numeric(value):
        """ Test if a value is numeric. """
        return isinstance(value, int) or isinstance(value, float)

    def match(self, example):
        # Compare the feature value in an example to the
        # feature value in this question.
        val = example[self.__column]
        if self.is_numeric(val):
            return val >= self.__value
        else:
            return val == self.__value

    def __str__(self):
        # This is just a helper method to print
        # the question in a readable format.
        condition = "=="
        if self.is_numeric(self.__value):
            condition = ">="
        return "Is %s %s %s?" % (
            self.__header[self.__column], condition, str(self.__value))
