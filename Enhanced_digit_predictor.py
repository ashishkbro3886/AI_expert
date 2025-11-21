# import tensorflow as tf

# from tensorflow.keras import layers, models

# import matplotlib.pyplot as plt

# from tensorflow.keras.preprocessing.image import ImageDataGenerator

 

# # Load MNIST dataset

# (x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

 

# # Normalize the data

# x_train, x_test = x_train / 255.0, x_test / 255.0

 

# # Reshape the data to fit the neural network

# x_train = x_train.reshape(-1, 28 * 28)

# x_test = x_test.reshape(-1, 28 * 28)

 

# # Data Augmentation

# datagen = ImageDataGenerator(

#     rotation_range=10,

#     zoom_range=0.1,

#     width_shift_range=0.1,

#     height_shift_range=0.1

# )

 

# datagen.fit(x_train)

 

# # Build the model

# model = models.Sequential([

#     layers.Flatten(input_shape=(28, 28)),

#     layers.Dense(128, activation=tf.keras.layers.LeakyReLU(alpha=0.1)),

#     layers.Dense(64, activation=tf.keras.layers.LeakyReLU(alpha=0.1)),

#     layers.Dense(10, activation='softmax')

# ])

 

# # Compile the model

# model.compile(optimizer='rmsprop',

#               loss='sparse_categorical_crossentropy',

#               metrics=['accuracy'])

 

# # Train the model with augmented data

# model.fit(datagen.flow(x_train, y_train, batch_size=32), epochs=10)

 

# # Evaluate the model

# test_loss, test_acc = model.evaluate(x_test, y_test)

# print(f"Test accuracy: {test_acc}")

 

# # Make predictions

# predictions = model.predict(x_test)

 

# # Display the first image and prediction

# plt.imshow(x_test[0], cmap=plt.cm.binary)

# plt.title(f"Predicted: {predictions[0].argmax()}")

# plt.show()

import tensorflow as tf
from tensorflow.keras import layers, models
import matplotlib.pyplot as plt
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# Load MNIST dataset
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

# Reshape to 4D (batch, height, width, channels)
x_train = x_train.reshape(-1, 28, 28, 1).astype("float32") / 255.0
x_test = x_test.reshape(-1, 28, 28, 1).astype("float32") / 255.0

# Data Augmentation
datagen = ImageDataGenerator(
    rotation_range=10,
    zoom_range=0.1,
    width_shift_range=0.1,
    height_shift_range=0.1
)

datagen.fit(x_train)

# Build the model
model = models.Sequential([
    layers.Flatten(input_shape=(28, 28, 1)),
    layers.Dense(128, activation=tf.keras.layers.LeakyReLU(alpha=0.1)),
    layers.Dense(64, activation=tf.keras.layers.LeakyReLU(alpha=0.1)),
    layers.Dense(10, activation='softmax')
])

# Compile the model
model.compile(optimizer='rmsprop',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Train the model with augmented data
model.fit(datagen.flow(x_train, y_train, batch_size=32), epochs=10)

# Evaluate the model
test_loss, test_acc = model.evaluate(x_test, y_test)
print(f"Test accuracy: {test_acc}")

# Make predictions
predictions = model.predict(x_test)

# Display the first image and prediction
plt.imshow(x_test[0].reshape(28, 28), cmap=plt.cm.binary)
plt.title(f"Predicted: {predictions[0].argmax()}")
plt.show()
