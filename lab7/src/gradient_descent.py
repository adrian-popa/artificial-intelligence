import numpy as np


def gradient_descent(X, y, theta, alpha=0.01, iterations=1000):
    theta_history = np.matrix(np.zeros((1, 5)))
    cost_history = np.zeros(iterations)

    # iterate for the given number of times and calculate the cost
    for i in range(iterations):
        cost = (X * transpose(theta)) - y

        # iterate through all 5 attributes
        for j in range(5):
            prediction = np.multiply(cost, X[:, j])
            theta_history[0, j] = theta[0, j] - ((alpha / len(X)) * np.sum(prediction))

        theta = theta_history
        cost_history[i] = compute_cost(X, y, theta)

    return theta, cost_history


def compute_cost(X, y, theta):
    inner = np.power(((X * transpose(theta)) - y), 2)
    return np.sum(inner) / (2 * len(X))


def transpose(matrix):
    array = np.asarray(matrix)
    aux = array.transpose()
    return np.matrix(aux)
