import numpy as np


class NeuralNetwork:

    # constructor for this VERY particular network with 2 layers (plus one for input)
    def __init__(self, x, y, hidden):
        self.input = x
        self.weights1 = np.random.rand(self.input.shape[1], hidden)
        self.weights2 = np.random.rand(hidden, 1)
        self.y = y
        self.output = np.zeros(self.y.shape)
        self.loss = []
        self.layer1 = None

    # the function that computes the output of the network for some input
    def feedforward(self):
        self.layer1 = np.dot(self.input, self.weights1)
        self.output = np.dot(self.layer1, self.weights2)

    # the back propagation algorithm
    def backprop(self, l_rate):
        # application of the chain rule to find derivative of the
        # loss function with respect to weights2 and weights1
        d_weights2 = np.dot(self.layer1.T, self.y - self.output)

        d_weights1 = np.dot(self.input.T, (np.dot(self.y - self.output, self.weights2.T)))
        # update the weights with the derivative (slope) of the loss function

        self.weights1 += l_rate * d_weights1
        self.weights2 += l_rate * d_weights2
        self.loss.append(sum((self.y - self.output)))
