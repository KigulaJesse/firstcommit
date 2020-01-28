from __future__ import absolute_import, division, print_function, unicode_literals

#tensorflow and tf.keras
import tensorflow as tf
from tensorflow import keras

#helper libraries
import numpy as np
import matplotlib.pyplot as plt

fashion_mnist = keras.datasets.fashion_mnist
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat', 'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

#print(train_images.shape)
#print(train_labels)

#plt.figure()
#plt.imshow(train_images[0],interpolation = 'nearest')
#plt.colorbar()
#plt.grid(False)
#plt.show()

train_images = train_images / 255.0
test_images = test_images /255.0

#print(train_images)

plt.figure(figsize=(10,10))
for i in range (25):
	plt.subplot(5,2*5,i+1)
	plt.xticks([])
	plt.yticks([])
	plt.grid(True)
	plt.imshow(train_images[i],cmap=plt.cm.gray,interpolation='bicubic')
	plt.xlabel(class_names[train_labels[i]])
plt.show()

model = keras.Sequential([
keras.layers.Flatten(input_shape=(28,28)),
keras.layers.Dense(128,activation='relu'),
keras.layers.Dense(10,activation='softmax')
])

model.compile(optimizer='adam',
	loss='sparse_categorical_crossentropy',
	metrics=['accuracy'])
model.fit(train_images, train_labels, epochs=10)

test_loss, test_acc = model.evaluate(test_images, test_labels, verbose=2)

#print('\nTest accuracy:',test_acc)
predictions = model.predict(test_images)
"""print(predictions[1])
#print(class_names[test_labels[1]])
print(class_names[np.argmax(predictions[999])])
print(class_names[test_labels[999]])"""

def plot_image(i, predictions_array, true_label, img):
	predictions_array, true_label, img = predictions_array, true_label[i], img[i]
	plt.grid(False)
	plt.xticks([])
	plt.yticks([])

	plt.imshow(img, cmap=plt.cm.binary, interpolation = 'bicubic')

	predicted_label = np.argmax(predictions_array)
	if predicted_label == true_label:
		color = 'blue'
	else:
		color = 'red'

	plt.xlabel("{} {:2.0f}% ({})".format(class_names[predicted_label],
                                100*np.max(predictions_array),
                                class_names[true_label]),
                                color=color)

def plot_value_array(i, predictions_array, true_label):
	predictions_array, true_label = predictions_array, true_label[i]
	plt.grid(False)
	plt.xticks(range(10))
	plt.yticks([])
	thisplot = plt.bar(range(10), predictions_array, color ="#777777")
	plt.ylim([0, 1])
	predicted_label = np.argmax(predictions_array)
	thisplot[predicted_label].set_color('red')
	thisplot[true_label].set_color('blue')	


num_rows = 5
num_cols = 3
num_images = num_rows * num_cols
plt.figure(figsize=(2*2*num_cols,2*num_rows))
for i in range(num_images):
	plt.subplot(num_rows, num_cols, 2*i+1)
	plot_image(i,predictions[i],test_labels,test_images)
	plt.subplot(num_rows, num_cols, 2*i+2)
	plot_value_array(i,predictions[i],test_labels)

plt.tight_layout()
plt.show()




























