class Leaf:
    """
    A Leaf node classifies data.
    This holds a dictionary of class (e.g., "L") -> number of times
    it appears in the rows from the training data that reach this leaf.
    """

    def __init__(self, predictions):
        self.predictions = predictions
