from models.decision_node import DecisionNode
from models.leaf import Leaf
from models.question import Question


class DecisionTree:

    def __init__(self, header, training_data):
        self.__header = header

        self.__tree = self.__build_tree(training_data)

    def __build_tree(self, rows):
        """
        Builds the tree.
        """

        # Try partitioning the dataset on each of the unique attribute,
        # calculate the information gain and return the question that produces the highest gain.
        gain, question = self.find_best_split(rows)

        # Base case: no further info gain
        # Since we can ask no further questions, we'll return a leaf.
        if gain == 0:
            predictions = self.class_counts(rows)
            return Leaf(predictions)

        # If we reach here, we have found a useful feature / value to partition on.
        true_rows, false_rows = self.partition(rows, question)

        # Recursively build the true branch.
        true_branch = self.__build_tree(true_rows)

        # Recursively build the false branch.
        false_branch = self.__build_tree(false_rows)

        # Return a Question node.
        # This records the best feature / value to ask at this point,
        # as well as the branches to follow depending on the answer.
        return DecisionNode(question, true_branch, false_branch)

    def get_tree(self):
        """ Returns the generated decision tree. """
        return self.__tree

    @staticmethod
    def unique_values(rows, col):
        """ Find the unique values for a column in a dataset. """
        return set([row[col] for row in rows])

    @staticmethod
    def class_counts(rows):
        """ Counts the number of each type of example in a dataset. """
        counts = {}  # a dictionary of label -> count.
        for row in rows:
            label = row[0] # in our dataset format, the label is always the first column
            if label not in counts:
                counts[label] = 0
            counts[label] += 1
        return counts

    @staticmethod
    def partition(rows, question):
        """
        Partitions a dataset.
        For each row in the dataset, check if it matches the question. If
        so, add it to 'true rows', otherwise, add it to 'false rows'.
        """
        true_rows, false_rows = [], []
        for row in rows:
            if question.match(row):
                true_rows.append(row)
            else:
                false_rows.append(row)
        return true_rows, false_rows

    def gini(self, rows):
        """
        Calculate the Gini Impurity for a list of rows.
        """
        counts = self.class_counts(rows)
        impurity = 1
        for lbl in counts:
            prob_of_lbl = counts[lbl] / float(len(rows))
            impurity -= prob_of_lbl ** 2
        return impurity

    def info_gain(self, left, right, current_uncertainty):
        """
        Information Gain.
        The uncertainty of the starting node, minus the weighted impurity of two child nodes.
        """
        p = float(len(left)) / (len(left) + len(right))
        return current_uncertainty - p * self.gini(left) - (1 - p) * self.gini(right)

    def find_best_split(self, rows):
        """ Find the best question to ask by iterating over every feature / value
        and calculating the information gain. """
        best_gain = 0  # keep track of the best information gain
        best_question = None  # keep train of the feature / value that produced it
        current_uncertainty = self.gini(rows)
        n_features = len(rows[0]) - 1  # number of columns minus one

        for col in range(1, n_features + 1):  # for each feature
            values = set([row[col] for row in rows])  # unique values in the column

            for val in values:  # for each value
                question = Question(self.__header, col, val)

                # try splitting the dataset
                true_rows, false_rows = self.partition(rows, question)

                # Skip this split if it doesn't divide the dataset.
                if len(true_rows) == 0 or len(false_rows) == 0:
                    continue

                # Calculate the information gain from this split
                gain = self.info_gain(true_rows, false_rows, current_uncertainty)

                if gain >= best_gain:
                    best_gain, best_question = gain, question

        return best_gain, best_question
