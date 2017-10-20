import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

# 随机生成1000个点，围绕在y=0.1x+0.3的直线周围
num_points = 1000  #定义点的数量
vectors_set = []   #定义空的集合
for i in range(num_points):
    x1 = np.random.normal(0.0, 0.55)                   #使用random函数生产x1
    y1 = x1 * 0.1 + 0.3 + np.random.normal(0.0, 0.03)
    vectors_set.append([x1, y1])                       #把生产好的点放到 集合中去

# 生成一些样本
x_data = [v[0] for v in vectors_set]
y_data = [v[1] for v in vectors_set]

##scatter这
plt.scatter(x_data, y_data, c='r')
plt.show()






# 生成1维W矩阵，取值是[-1, 1]之间的随机数
W = tf.Variable(tf.random_uniform([1], -1.0, 1.0), name='W')
# 生成1维b矩阵，初始值是0
b = tf.Variable(tf.zeros([1]), name='b')
# 经过计算取得预估值y
y = W * x_data + b

# 以预估值y和实际值y_data之间的均方误差作为损失
loss = tf.reduce_mean(tf.square(y - y_data), name='loss')
# 采用梯度下降法来优化参数
optimizer = tf.train.GradientDescentOptimizer(0.5)      ##那0.5是什么意思呢
# 训练的过程就是最小化这个误差值
train = optimizer.minimize(loss, name='train')

sess = tf.Session()        #这种定义session的方法也可以，但是不推荐。

#对所有变量进行初始化
init = tf.global_variables_initializer()
# 上面定义的都没有运算，直到 sess.run 才会开始运算
sess.run(init)

# 初始化的w和b是多少
print("W=", sess.run(W), "b=", sess.run(b), "loss=", sess.run(loss))
# 执行20次训练
for step in range(20):
    sess.run(train)
    # 输出训练好的W和b
    print("W=", sess.run(W), "b=", sess.run(b), "loss=", sess.run(loss))

print("迭代后：W=", sess.run(W), "迭代后：b=", sess.run(b), "迭代后：loss=", sess.run(loss))