from neural_network import *
import matplotlib as mpl
import matplotlib.pyplot as plt
import random


def main():
    # X the array of inputs, Y the array of outputs, 4 pairs in total
    inputs, outputs = load_data('bdate2.txt')

    train_X = []
    train_Y = []
    test_X = []
    test_Y = []

    train_length = int((len(inputs) * 0.8))

    # random order
    c = list(zip(inputs, outputs))
    random.shuffle(c)
    inputs, outputs = zip(*c)

    for i in range(len(inputs)):
        if i < train_length:
            train_X.append(inputs[i])
            train_Y.append(outputs[i])
        else:
            test_X.append(inputs[i])
            test_Y.append(outputs[i])

    X = np.array([np.array(row) for row in train_X])
    Y = np.array([np.array(row) for row in train_Y])

    nn = NeuralNetwork(X, Y, train_length)

    nn.loss = []
    iterations = []
    for i in range(4000):
        nn.feedforward()
        nn.backprop(0.00000001)
        iterations.append(i)

    w = nn.weights2
    diff = 0

    for tx, ty in zip(test_X, test_Y):
        predict = w[0] * tx[0] + w[1] * tx[1] + w[2] * tx[2] + w[3] * tx[3] + w[4] * tx[4]
        d = abs(ty[0] - predict)
        diff += d
    avg = diff / len(test_X)

    print('Average difference:', avg)

    mpl.pyplot.plot(iterations, nn.loss, label='loss value vs iteration')
    mpl.pyplot.xlabel('Iterations')
    mpl.pyplot.ylabel('Loss function')
    mpl.pyplot.legend()
    mpl.pyplot.show()


def load_data(filename):
    with open(filename, 'r') as file:
        inputs = []
        outputs = []

        for line in file:
            if line != '\n':
                data = line.strip().split(' ')
                inputs.append([float(data[i]) for i in range(5)])
                outputs.append([float(data[5])])

    return inputs, outputs


main()
