import tensorflow as tf
import math

probs = tf.constant([
    [0.1, 0.9],
    [0.2, 0.8]
])
labels = tf.constant([1, 0])
alpha = tf.constant(0.25, dtype=tf.float32)
gamma = tf.constant(2, dtype=tf.float32)
epsilon = 1.e-8
y_true = tf.one_hot(labels, depth=2, dtype=tf.float32)
y_pred = tf.clip_by_value(probs, epsilon, 1. - epsilon)
p_t = y_true * y_pred + (tf.ones_like(y_true) - y_true) * (tf.ones_like(y_true) - y_pred)
weight = tf.pow((tf.ones_like(y_true) - p_t), gamma)
alpha_t = y_true * alpha + (tf.ones_like(y_true) - y_true) * (1 - alpha)
focal_loss = - alpha_t * weight * tf.log(p_t)
per_example_loss = tf.layers.flatten(focal_loss[:, -1])
loss = tf.reduce_mean(per_example_loss)
with tf.Session() as sess:
    print(sess.run(alpha_t))
    print(sess.run(weight))
    print(sess.run(tf.log(p_t)))
    print(sess.run(focal_loss))
    print(sess.run(per_example_loss))
