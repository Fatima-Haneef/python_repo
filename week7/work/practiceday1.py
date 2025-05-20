# # import tensorflow as tf 

# # # a = tf.constant([[1,2],[3,4]])
# # # b = tf.constant([[5,6],[7,8]])
# # # print("sum:\n", tf.add(a,b))
# # # print("multiply:\n", tf.multiply(a,b))
# # # print("subtract:\n", tf.subtract(a,b))
# # # print("divide:\n", tf.divide(a,b))
# # # print("sum off all elements:\n", tf.reduce_sum(a))
# # # print("sum off all elements:\n", tf.reduce_sum(b))


# # # tf.random.set_seed(1)
# # # x = tf.random.normal([3,2], mean=0.0, stddev=1)
# # # print("x:\n", x)
# # # print(tf.reduce_sum(x))



# # # scaler = tf.constant(5)
# # # print(scaler)


# # # vector = tf.constant([1,2,3])
# # # print(vector)

# # # matrix = tf.constant([1,2,3],[4,5,6])
# # # print(matrix)

# # # tensor_3d = tf.constant([[1],[2]],[[3],[4]])
# # # print(tensor_3d)


# # # t = tf.constant([[1,2,3],[4,5,6]])
# # # print(t.shape)
# # # print(t.dtype)
# # # print(t.ndim)
# # # print(tf.rank(t))


# # # float_tensor = tf.constant([[1.0,2.0,3.0],[4.0,5.0,6.0]], dtype=tf.float32)
# # # bool_tensor = tf.constant([[True, False, True],[False, True, False]], dtype=tf.bool)
# # # string_tensor = tf.constant([[b"hello", b"world"], [b"foo", b"bar"]], dtype=tf.string)
# # # print(string_tensor)
# # # print(float_tensor)
# # # print(bool_tensor)



# # # tgg = tf.constant([[1, 2], [3, 4], [5, 6]])
# # # reshaped = tf.reshape(tgg, [2, 3])
# # # print(reshaped)


# # # x = tf.constant([1,2,3])
# # # x_expanded = tf.expand_dims(x, axis=1)  # Add a new dimension at axis 0
# # # print(x_expanded)

# # # y = tf.constant([[[1],[2],[3]]])
# # # y_squeezed = tf.squeeze(y)  # Remove dimensions of size 1
# # # print(y_squeezed)



# # # x = tf.constant([
# # #  [
# # #     [1, 2],
# # #     [3, 4]
# # #   ],
# # #   [
# # #     [5, 6],
# # #     [7, 8]
# # #   ]
# # # ])

# # # print(x.shape)



# # # t = tf.constant([[1,2,3],[4,5,6]])
# # # print(t[0])
# # # print(t[:,1])



# import tensorflow as tf

# from tensorflow.keras import datasets, layers, models
# import matplotlib.pyplot as plt

# (train_images, train_labels), (test_images, test_labels) = datasets.cifar10.load_data()

# # Normalize pixel values to be between 0 and 1
# train_images, test_images = train_images / 255.0, test_images / 255.0

# class_names = ['airplane', 'automobile', 'bird', 'cat', 'deer',
#                'dog', 'frog', 'horse', 'ship', 'truck']

# plt.figure(figsize=(10,10))
# for i in range(25):
#     plt.subplot(5,5,i+1)
#     plt.xticks([])
#     plt.yticks([])
#     plt.grid(False)
#     plt.imshow(train_images[i])
#     # The CIFAR labels happen to be arrays, 
#     # which is why you need the extra index
#     plt.xlabel(class_names[train_labels[i][0]])
# plt.show()

# model = models.Sequential()
# model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)))
# model.add(layers.MaxPooling2D((2, 2)))
# model.add(layers.Conv2D(64, (3, 3), activation='relu'))
# model.add(layers.MaxPooling2D((2, 2)))
# model.add(layers.Conv2D(64, (3, 3), activation='relu'))

# model.summary()

# model.add(layers.Flatten())
# model.add(layers.Dense(64, activation='relu'))
# model.add(layers.Dense(10))

# model.summary()

# model.compile(optimizer='adam',
#               loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
#               metrics=['accuracy'])

# history = model.fit(train_images, train_labels, epochs=10, 
#                     validation_data=(test_images, test_labels))


# plt.plot(history.history['accuracy'], label='accuracy')
# plt.plot(history.history['val_accuracy'], label = 'val_accuracy')
# plt.xlabel('Epoch')
# plt.ylabel('Accuracy')
# plt.ylim([0.5, 1])
# plt.legend(loc='lower right')

# test_loss, test_acc = model.evaluate(test_images,  test_labels, verbose=2)

# print(test_acc)

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense

# Load MNIST data
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

# Preprocess data
x_train = x_train.reshape(-1, 28, 28, 1).astype("float32") / 255.0
x_test = x_test.reshape(-1, 28, 28, 1).astype("float32") / 255.0

# Build CNN model
model = Sequential([
    Conv2D(filters=32, kernel_size=(3, 3), activation='relu', padding='same', input_shape=(28, 28, 1)),
    MaxPooling2D(pool_size=(2, 2)),
    Flatten(),
    Dense(units=10, activation='softmax')
])

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Train
model.fit(x_train, y_train, epochs=5, validation_split=0.1)

# Evaluate
model.evaluate(x_test, y_test)
