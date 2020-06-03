import numpy as np

# TensorFlow
import tensorflow.keras.datasets.mnist as mnist

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Dense, Flatten
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.optimizers import SGD

# Load the MNIST dataset
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

# train_images = mnist.train_images()
# train_labels = mnist.train_labels()
# test_images = mnist.test_images()
# test_labels = mnist.test_labels()

train_images = (train_images / 255) - 0.5
test_images = (test_images / 255) - 0.5

train_images = np.expand_dims(train_images, axis=3)
test_images = np.expand_dims(test_images, axis=3)

model = Sequential([
    Conv2D(8, 3, input_shape=(28, 28, 1), use_bias=False),
    MaxPooling2D(pool_size=2),
    Flatten(),
    Dense(10, activation='softmax'),
])

model.compile(SGD(lr=.005), loss='categorical_crossentropy', metrics=['accuracy'])

model.fit(
    train_images,
    to_categorical(train_labels),
    batch_size=1,
    epochs=3,
    validation_data=(test_images, to_categorical(test_labels)),
)
