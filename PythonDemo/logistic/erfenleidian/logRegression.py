#################################################
# logRegression: Logistic Regression
# Author : panpan
# Date   : 2017-09-20
# Email  : panpan668706@163.com
#################################################

from numpy import *
import matplotlib.pyplot as plt
import time


# 首先来计算 sigmoid函数
def sigmoid(inX):
    return 1.0 / (1 + exp(-inX))


# train a logistic regression model using some optional optimize algorithm
# input: train_x is a mat datatype, each row stands for one sample
#        train_y is mat datatype too, each row is the corresponding label
#        opts is optimize option include step and maximum number of iterations

#训练Logistic回归模型，使用一些可选的优化算法
#输入：train_x是mat类型，每行代表一个样本
# train_y是mat的数据类型，每一行对应的标签
#选择优化选项包括步骤和最大迭代次数


#备注：在做deeplearning过程中，使用caffe的框架，一般使用matlab来处理图片（matlab处理图片相对简单，高效），
#用python来生成需要的lmdb文件以及做test产生结果。所以某些matlab从图片处理得到的label信息都会以.mat文件供python读取，
#同时也python产生的结果信息也需要matlab来做进一步的处理（当然也可以使用txt，不嫌麻烦自己处理结构信息）。


def trainLogRegres(train_x, train_y, opts):
    # calculate training time
    startTime = time.time()#当前开始时间
#它的功能是读取矩阵的长度，比如shape[0]就是读取矩阵第一维度的长度。
#它的输入参数可以使一个整数表示维度，也可以是一个矩阵。这么说你可能不太理解，我们还是用各种例子来说明他的用法：
    numSamples, numFeatures = shape(train_x)
#取到优化项
    alpha = opts['alpha'];
#取到最大迭代次数
    maxIter = opts['maxIter']
#权重先随机给出
    weights = ones((numFeatures, 1))

    # 通过梯度下降优化algorilthm  就是说用梯度上升方法求出回归系数

    for k in range(maxIter):
        if opts['optimizeType'] == 'gradDescent':  # 梯度下降algorilthm
            output = sigmoid(train_x * weights)
            error = train_y - output
            weights = weights + alpha * train_x.transpose() * error
        elif opts['optimizeType'] == 'stocGradDescent':  # 随机梯度下降
            for i in range(numSamples):
                output = sigmoid(train_x[i, :] * weights)
                error = train_y[i, 0] - output
                weights = weights + alpha * train_x[i, :].transpose() * error
        elif opts['optimizeType'] == 'smoothStocGradDescent':  # 光滑随机梯度下降
            # 随机选择样本，减少波动的周期优化
            # 首先 回顾一下range 的方法 range(5) #代表从0到5(不包含5)  range(1,5) #代表从1到5(不包含5)
            dataIndex = range(numSamples)
            length = len(dataIndex)
            for i in range(numSamples):
                alpha = 4.0 / (1.0 + k + i) + 0.01
                #uniform() 方法将随机生成下一个实数，它在 [x, y) 范围内。
                randIndex = int(random.uniform(0, length))
                output = sigmoid(train_x[randIndex, :] * weights)
                error = train_y[randIndex, 0] - output
                weights = weights + alpha * train_x[randIndex, :].transpose() * error
                # print(randIndex)
               # del dataIndex[randIndex]  # 在一次迭代优化，删除样本 optimized sample
                length -=1
        else:
            raise NameError('Not support optimize method type!')
#当训练完 成后输出 成功
    print('训练完成! 共花费 %fs!' % (time.time() - startTime))

    return weights


# test your trained Logistic Regression model given test set
def testLogRegres(weights, test_x, test_y):
    numSamples, numFeatures = shape(test_x)
    matchCount = 0
    for i in range(numSamples):
        predict = sigmoid(test_x[i, :] * weights)[0, 0] > 0.5
        if predict == bool(test_y[i, 0]):
            matchCount += 1
    accuracy = float(matchCount) / numSamples
    return accuracy


# show your trained logistic regression model only available with 2-D data
def showLogRegres(weights, train_x, train_y):
    # notice: train_x and train_y is mat datatype
    numSamples, numFeatures = shape(train_x)
    if numFeatures != 3:
        print("Sorry! I can not draw because the dimension of your data is not 2!")

        return 1

        # draw all samples
    for i in range(numSamples):
        if int(train_y[i, 0]) == 0:
            plt.plot(train_x[i, 1], train_x[i, 2], 'or')
        elif int(train_y[i, 0]) == 1:
            plt.plot(train_x[i, 1], train_x[i, 2], 'ob')

            # 画线的分类
    min_x = min(train_x[:, 1])[0, 0]
    max_x = max(train_x[:, 1])[0, 0]
    weights = weights.getA()  # convert mat to array
    y_min_x = float(-weights[0] - weights[1] * min_x) / weights[2]
    y_max_x = float(-weights[0] - weights[1] * max_x) / weights[2]
    plt.plot([min_x, max_x], [y_min_x, y_max_x], '-g')
    plt.xlabel('X1');
    plt.ylabel('X2')
    plt.show()





def loadData():
    #初始化  训练数据
    train_x = []
    train_y = []

    #将数据读进来行进行分割
    fileIn = open('testSet.txt')
    for line in fileIn.readlines():
        #按照行进行分割  将文本中的每行中的字符一个个分开，变成list
        lineArr = line.strip().split()
        train_x.append([1.0, float(lineArr[0]), float(lineArr[1])])
        train_y.append(float(lineArr[2]))
    return mat(train_x), mat(train_y).transpose()


## step 1: load data
print("步骤 1: 加载数据...")

train_x, train_y = loadData()
test_x = train_x;
test_y = train_y

## step 2: training...
print("步骤二: 训练...")

opts = {'alpha': 0.01, 'maxIter': 20, 'optimizeType': 'smoothStocGradDescent'}
optimalWeights = trainLogRegres(train_x, train_y, opts)

## step 3: testing
print("步骤3：测试中...")
accuracy = testLogRegres(optimalWeights, test_x, test_y)

## 步骤4：显示结果
print("步骤4：显示结果...")

print('分类的精确率: %.3f%%' % (accuracy * 100))

showLogRegres(optimalWeights, train_x, train_y)