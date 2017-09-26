"""A very simple MNIST classifier.
See extensive documentation at
https://www.tensorflow.org/get_started/mnist/beginners
"""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import argparse
import sys
#这两行代码,MNIST数据托管在 Yann LeCun的网站上自动下载并自动读取数据：在我的博客中附有链接
from tensorflow.examples.tutorials.mnist import input_data
#要使用TensorFlow，首先我们需要导入它
import tensorflow as tf

FLAGS = None


def main(_):
  # Import data
  mnist = input_data.read_data_sets(FLAGS.data_dir, one_hot=True)

  # 我们通过操纵符号变量来描述这些交互操作。我们创建一个：
  #x不是具体的价值。这是一个placeholder值，当我们要求TensorFlow运行计算时，我们将输入一个值。
  # 我们希望能够输入任何数量的MNIST图像，每个图像被平铺成784维的向量。我们将其表示为具有形状的浮点数的2-D张量[None, 784]。
  # （这里None表示尺寸可以是任意长度。）
  x = tf.placeholder(tf.float32, [None, 784])
        # W具有[784,10]的形状，因为我们要将784维图像向量乘以它，以产生差分类的10维证据向量。
        # b具有[10]的形状，所以我们可以将其添加到输出。
  W = tf.Variable(tf.zeros([784, 10]))
  b = tf.Variable(tf.zeros([10]))
  y = tf.matmul(x, W) + b
        # It only takes one line to define it

  # Define loss and optimizer为了实现交叉熵，我们需要先添加一个新的占位符来输入正确答案：
  y_ = tf.placeholder(tf.float32, [None, 10])

  # The raw formulation of cross-entropy,
  #
  #   tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(tf.nn.softmax(y)),
  #                                 reduction_indices=[1]))
                # tf.reduce_sum adds the elements in the second dimension of y,
                # due to the reduction_indices=[1] parameter.
                # tf.reduce_mean computes the mean over all the examples in the batch.
  #
  # can be numerically unstable.
  #
  # So here we use tf.nn.softmax_cross_entropy_with_logits on the raw
  # outputs of 'y', and then average across the batch.

  cross_entropy = tf.reduce_mean(
      tf.nn.softmax_cross_entropy_with_logits(labels=y_, logits=y))
  train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)
        # apply your choice of optimization algorithm to modify the variables and reduce the loss.

  sess = tf.InteractiveSession()
        # launch the model in an InteractiveSession
  tf.global_variables_initializer().run()
        # 我们首先必须创建一个操作来初始化我们创建的变量：

  # 我们来训练 - 我们将运行1000次训练步骤！
  for _ in range(1000):
    batch_xs, batch_ys = mnist.train.next_batch(100)
            # 循环的每一步，我们从训练集中得到一百个随机数据点的“批次”。我们运行train_step饲料中的批次数据来代替placeholders。
    sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})

  # 评估我们的模型
  correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
  # tf.argmax 是一个非常有用的功能，它给出沿某个轴的张量中最高条目的索引。
  # 例如，tf.argmax(y,1)我们的模型认为是每个输入最有可能的标签，而tf.argmax(y_,1)正确的标签。
  # 我们可以tf.equal用来检查我们的预测是否符合真相。
  accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
            # [True, False, True, True] would become [1,0,1,1] which would become 0.75.
  print(sess.run(accuracy, feed_dict={x: mnist.test.images,
                                      y_: mnist.test.labels}))
            # 对测试数据的准确性这应该是92％左右。

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('--data_dir', type=str, default='input_data',
                      help='Directory for storing input data')
  FLAGS, unparsed = parser.parse_known_args()
  tf.app.run(main=main, argv=[sys.argv[0]] + unparsed)