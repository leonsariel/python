# _*_ coding: utf-8 _*_
__author__ = 'Di Meng'
__date__ = '2/5/2018 9:37 PM'

import tensorflow as tf
import numpy as np

x_data = np.random.rand(100).astype(np.float32)
y_data = x_data * 0.1 + 0.3

weights = tf.Variable(tf.random_uniform([1], -1.0, 1.0))
biases = tf.Variable(tf.zeros([1]))

y = weights * x_data + biases

loss = tf.reduce_mean(tf.square(y - y_data))

# choose number less than 1
optimizer = tf.train.GradientDescentOptimizer(0.5)
train = optimizer.minimize(loss)

# need to init before run
init = tf.initialize_all_variables()

session = tf.Session()
session.run(init)

for step in range(201):
    session.run(train)
    if step % 20 == 0:
        print(step, session.run(weights), session.run(biases))


