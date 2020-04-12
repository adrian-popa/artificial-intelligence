from decision_tree import DecisionTree
from models.leaf import Leaf


def run():
    # Column labels.
    # These are used only to print the tree.
    headers = ["Class Name", "Left-Weight", "Left-Distance", "Right-Weight", "Right-Distance"]

    # The Balance Scale Weight & Distance Database
    # Format: each row is a new data.
    # The first column is the label.
    # The last four columns are features.
    training_data = read_data()

    decision_tree = DecisionTree(headers, training_data)

    balance_scale_tree = decision_tree.get_tree()

    print_tree(balance_scale_tree)

    # Evaluate
    # testing_data = read_data()
    testing_data = [
        ['L', 1, 3, 1, 2],
        ['B', 2, 3, 3, 2],
        ['R', 2, 5, 4, 4],
        ['R', 4, 1, 5, 5],
        ['L', 5, 3, 1, 1]
    ]

    for row in testing_data:
        print('Actual:', row[0], ', Predicted:', print_leaf(classify(row, balance_scale_tree)))

    print('\nTotal accuracy:', print_accuracy(testing_data, balance_scale_tree))


def read_data():
    data = []

    file = open('balance-scale.data', 'r')

    for line in file:
        c, lw, ld, rw, rd = line.split(',')
        attributes = [c, int(lw), int(ld), int(rw), int(rd)]
        data.append(attributes)

    file.close()

    return data


def print_tree(node, spacing=""):
    # Base case: we've reached a leaf
    if isinstance(node, Leaf):
        print(spacing + "Predict", node.predictions)
        return

    # Print the question at this node
    print(spacing + str(node.question))

    # Call this function recursively on the true branch
    print(spacing + '--> True:')
    print_tree(node.true_branch, spacing + "  ")

    # Call this function recursively on the false branch
    print(spacing + '--> False:')
    print_tree(node.false_branch, spacing + "  ")


def print_leaf(counts):
    """ A nicer way to print the predictions at a leaf. """
    total = sum(counts.values()) * 1.0
    probs = {}
    for lbl in counts.keys():
        probs[lbl] = str(int(counts[lbl] / total * 100)) + "%"
    return probs


def classify(row, node):
    # Base case: we've reached a leaf
    if isinstance(node, Leaf):
        return node.predictions

    # Decide whether to follow the true-branch or the false-branch.
    # Compare the feature / value stored in the node,
    # to the example we're considering.
    if node.question.match(row):
        return classify(row, node.true_branch)
    else:
        return classify(row, node.false_branch)


def print_accuracy(rows, tree):
    accurate_predictions = 0

    for row in rows:
        counts = classify(row, tree)
        if len(counts.keys()) == 1:
            for lbl in counts.keys():
                if row[0] == lbl:
                    accurate_predictions += 1

    return str(accurate_predictions / len(rows) * 100) + '%'


run()
