import pandas as pd
from gradient_descent import *


def main():
    data = pd.read_csv('bdate2.txt', ' ', names=['Attr1', 'Attr2', 'Attr3', 'Attr4', 'Attr5', 'Result'])

    alpha = float(input('Give the alpha value (e.g. 0.05): '))
    iterations = int(input('Give the number of iteration: '))

    # normalize the data
    data = (data - data.mean()) / data.std()

    # insert ones column
    data.insert(0, 'Ones', 1)

    # set the values of X (training data) and y (targeted result)
    # where X represents the columns without the result
    X = data.iloc[:, 1:6]
    # where y represents the single column with the result
    y = data.iloc[:, 6:7]

    # convert data set to matrices and initialize theta
    X = np.matrix(X.values)
    y = np.matrix(y.values)
    theta = np.matrix(np.array([0, 0, 0, 0, 0]))

    theta_final, cost_history = gradient_descent(X, y, theta, alpha, iterations)

    # get the cost of the model
    cost_final = compute_cost(X, y, theta_final)

    print("\nTheta:", theta_final)
    print("Cost:", cost_final)


main()
