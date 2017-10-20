"""
自编码的实例
在MNIST数据集上采用自编码进行手写体识别
使用数据集:http://yann.lecun.com/exdb/mnist/
"""

from __future__ import division, print_function, absolute_import

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
#%matplotlib inline

# 导入数据
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("/home/panpan/PycharmProjects/test/com/Hub-panpan/ShibieImageDigit/input_data", one_hot=True)

# 参数
#步长 或学习速率
learning_rate = 0.01
#迭代多少次
training_epochs = 5
#批量大小
batch_size = 256
#迭代多少次打印一次结果
display_step = 1
examples_to_show = 10

# 网络参数
#第一层提取256个特征
n_hidden_1 = 256
#第二层提取128个特征
n_hidden_2 = 128
#输入数据28*28
n_input = 784
# tf Graph input (only pictures)
#实际shape[256,784]
X = tf.placeholder("float", [None, n_input])

# 权重参数
# encoder_h1=[784,256]
# encoder_h2=[256,128]
# decoder_h1=[128,256]
# decoder_h2=[256,784]

weights = {
    'encoder_h1': tf.Variable(tf.random_normal([n_input, n_hidden_1])),
    'encoder_h2': tf.Variable(tf.random_normal([n_hidden_1, n_hidden_2])),
    'decoder_h1': tf.Variable(tf.random_normal([n_hidden_2, n_hidden_1])),
    'decoder_h2': tf.Variable(tf.random_normal([n_hidden_1, n_input])),
}
biases = {
    'encoder_b1': tf.Variable(tf.random_normal([n_hidden_1])),
    'encoder_b2': tf.Variable(tf.random_normal([n_hidden_2])),
    'decoder_b1': tf.Variable(tf.random_normal([n_hidden_1])),
    'decoder_b2': tf.Variable(tf.random_normal([n_input])),
}

# 构建Encoder层
def encoder(x):
    # 第一层编码采用sigmoid激活函数 即对WX+b的结果采用Sigmoid进行激活
    #x->[256,784],w->[784,256]
    #layer_1->[256,256]
    layer_1 = tf.nn.sigmoid(tf.add(tf.matmul(x, weights['encoder_h1']),
                                   biases['encoder_b1']))
    # 第二层在第一层结果的基础上进行Sigmoid激活，即对WX1+b的结果进行Sigmoid激活，这里X1即为layer_1
    #layer_1->[256,256],w->[256,128]
    #layer_2->[256,128]
    layer_2 = tf.nn.sigmoid(tf.add(tf.matmul(layer_1, weights['encoder_h2']),
                                   biases['encoder_b2']))
    return layer_2



# 其次 我们要设计一个解码器
# 构建decoder层
def decoder(x):
    # 对编码层的结果进行解码，这里相当于做一个反向的还原
    # x=layer_2->[256,128],w->[128,256]
    # 解码结果layer_1->[256,256]
    layer_1 = tf.nn.sigmoid(tf.add(tf.matmul(x, weights['decoder_h1']),
                                   biases['decoder_b1']))
    # 对上面的结果进行再次解码
    # w->[256,784]
    # 结果layer_2->[256,784] 相当于对图像做了一次还原
    layer_2 = tf.nn.sigmoid(tf.add(tf.matmul(layer_1, weights['decoder_h2']),
                                   biases['decoder_b2']))
    return layer_2



# 构造模型
#先编码
encoder_op = encoder(X)
#再解码
decoder_op = decoder(encoder_op)

# 解码后的结果，就相当于是预测的结果
y_pred = decoder_op
# Targets (Labels) are the input data.
y_true = X

# 定义损失函数，这里采用误差平方的均值
cost = tf.reduce_mean(tf.pow(y_true - y_pred, 2))
# 采用RMS方法进行优化
optimizer = tf.train.RMSPropOptimizer(learning_rate).minimize(cost)

# 初始化变量
init = tf.global_variables_initializer()

# 开始构建Graph
with tf.Session() as sess:
    sess.run(init)
    #总共计算批次
    total_batch = int(mnist.train.num_examples/batch_size)
    # 总共进行20次循环迭代
    for epoch in range(training_epochs):
        # 遍历每个批次
        for i in range(total_batch):
            batch_xs, batch_ys = mnist.train.next_batch(batch_size)
            # 迭代优化
            _, c = sess.run([optimizer, cost], feed_dict={X: batch_xs})
        # 这里if没什么意义，如果display_step不是1的话则有意义，表示多少次打印一次结果
        if epoch % display_step == 0:
            print("迭代次数:", '%04d' % (epoch+1),
                  "损失值=", "{:.9f}".format(c))

    print("优化完成")

    # 在测试集上进行自编码的测试
    encode_decode = sess.run(
        y_pred, feed_dict={X: mnist.test.images[:examples_to_show]})
    # 线性化的对比测试结果Compare original images with their reconstructions
    f, a = plt.subplots(2, 10, figsize=(10, 2))
    for i in range(examples_to_show):
        a[0][i].imshow(np.reshape(mnist.test.images[i], (28, 28)))
        a[1][i].imshow(np.reshape(encode_decode[i], (28, 28)))
    f.show()
    plt.draw()
    plt.waitforbuttonpress()

