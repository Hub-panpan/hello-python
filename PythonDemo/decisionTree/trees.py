'''
Created on 11 2017
Decision Tree Source Code for Machine Learning in Action Ch. 3
@author: panpan
'''
from math import log
#导入数学运算log
import operator
#创建数据
def createDataSet():
    #高中化学中 也学过熵的概念
    #最后一列出现不同标签的数量越高，则熵越大，代表无序程序越高，我们在数据集中添加的分类就越多
    dataSet = [[1,1,'yes'],
               [1,1,'yes'],
               [1,0,'no'],
               [0,1,'no'],
               [0,1,'no']]
    labels = ['no surfacing','flippers']
    return dataSet,labels#在这里，数据集是针对标签的，第一个数据对应第一个标签，最后一个数据代表判断标签
#计算原始的信息熵


def calcShannonEnt(dataSet):
    numEntries = len(dataSet)#得到数据集的实例个数
    labelCounts = {}#初始化一个字典用于存储键值和对应的出现次数
    for featVec in dataSet:
        currentLabel = featVec[-1]#获取每行最后一个数值，作为键值
        if currentLabel not in labelCounts.keys():#如果当前键值不存在，则将键值添加进字典，键值对应的数值为0,意思是出现零次，若存在，则数值加1,代表出现次数多一次
            labelCounts[currentLabel] = 0
        labelCounts[currentLabel] += 1
    shannonEnt = 0.0#用所有标签的发生概率计算香农熵
    for key in labelCounts:#使用所有类标签的发生频率计算类别出现的概率。我们将用这个概率计算香农熵，统计所有类标签发生的次数
        prob = float(labelCounts[key])/numEntries
        shannonEnt -= prob*log(prob,2)# #以2为底数求对数
    return shannonEnt


#返回某个特征中某个值所有的数据样例
def splitDataSet(dataSet,axis,value):#输入：待划分的数据集，划分数据集的特征，需要返回的特征的值
    retDataSet = []#python不考虑内存问题，在函数中传递的是列表的引用，在函数内部是对列表对象的更改，将会影响该列表对象的整个生存周期。为了消除影响，新建一个列表对象。
    for featVec in dataSet:
        if featVec[axis] == value:#数据集中每个元素都是列表，遍历每个元素，发现符合的就添加到列表中;当按照某个特征划分数据集时，需要将所有符合的元素抽取出来。感觉运行结果是第axis个元素的值为value时，抽取这个元素。
            reducedFeatVec = featVec[:axis]#当axis为0时，0：0是空;0：1是0的值
            reducedFeatVec.extend(featVec[axis+1:])#extend是把两个列表合并
            retDataSet.append(reducedFeatVec)#append是把后一个列表直接当作一个元素添加进前一个列表
    return retDataSet


"""计算信息增益最大的特征，并返回对应的特征索引 
选取特征值，划分数据集，计算出最好的划分数据集的特征"""
def chooseBestFeatureToSplit(dataSet):#dataSet需是一种由列表元素组成的列表，所有的列表元素都要具有相同的数据长度;数据的最后一列或每个元素的做后一列都是当前元素的标签。list中数据类型不限，不影响。
    numFeatures = len(dataSet[0])-1#判定在每个元素列表中包含多少个特征属性，最后一个是标签，要去掉。
    baseEntropy = calcShannonEnt(dataSet)#计算整个数据集的原始熵，这个无序度用于与划分完之后的数据集的熵值进行比较。
    bestInfoGain = 0.0;bestFeature = -1#初始化最佳信息增益和最佳特征索引
    for i in range(numFeatures):#遍历所有特征
        featList = [example[i] for example in dataSet]#把第i个索引所对应的值提取出来
        uniqueVals = set(featList)#把提出来的值唯一化，set是集合数据类型，值不相同
        newEntropy = 0.0#初始化新熵
        for value in uniqueVals:#遍历当前特征中的唯一属性值，对每个特征划分一次数据集
            subDataSet = splitDataSet(dataSet,i,value)#计算数据集的新熵值，并对所有唯一特征值得到的熵求和
            prob = len(subDataSet)/float(len(dataSet))#子集占总集的元素数量百分比
            newEntropy += prob * calcShannonEnt(subDataSet)
        infoGain = baseEntropy - newEntropy#这就得到信息增益，是熵的减少，无序度的减少
        if (infoGain > bestInfoGain):#比较信息增益，得到最大值
            bestInfoGain = infoGain
            bestFeature = i
    return bestFeature#返回最好特征划分的索引值
#分类的少数服从多数的机制
"""得到每个类标签出现的次数，返回出现次数最多的分类名称"""
def majorityCnt(classList):
    classCount={}
    for vote in classCount:
        if vote not in classCount.keys():classCount[vote] = 0
        classCount[vote] += 1
    sortedClassCount = sorted(classCount.iteritem(),key=operator.itemgetter(1),reverse = true) #对标签出现的频率按从大到小进行排序
    return sortedClassCount[0][0] #返回出现频率最大的那个标签作为子集的标签。

#根据数据集和标签，创建一个决策树。
#递归构建决策树,这是这个文件的主函数，对已有的数据集，知调用这一个函数就创建了决策树******************************************
def createTree(dataSet,labels):#输入：数据集和标签列表，标签列表中集中所有特征的标签，算法本身不需要，只作为输入参数提供
    classList = [example[-1] for example in dataSet]#提取数据集最后一列数据
    if classList.count(classList[0]) == len(classList):#当计算在最后一列数据中与第一个值相同的元素个数与最后一列数据个数相同时，直接返回第一个元素值，意思是所有类标签都相同
        return classList[0]
    if len(dataSet[0]) == 1:#当数据集中第一个也代表所有元素的长度为1时，仍然类标签不相同，就挑选出现次数最多的作为返回值
        return majorityCnt(classList)
    bestFeat = chooseBestFeatureToSplit(dataSet)#返回最佳特征值划分的索引
    bestFeatLabel = labels[bestFeat]#得到最佳特征值索引的标签
    myTree = {bestFeatLabel:{}}#使用字典类型存储树的信息
    del(labels[bestFeat])#从标签列表中删除最好特征值对应的那个标签
    featValues = [example[bestFeat] for example in dataSet]#得到最佳特征值对应的数据集中的那一列数据组成列表
    uniqueVals = set(featValues)#唯一化
    for value in uniqueVals:#遍历唯一化列表
        subLabels = labels[:]#复制类标签，当函数参数是列表类型时，参数是按照引用方式传递的，保证每次调用函数时都不改变原始列表的内容，就是开一块新内存。
        myTree[bestFeatLabel][value] = createTree(splitDataSet(dataSet,bestFeat,value),subLabels)#等号前第一个中括号是指字典键值，键值可任意类型;第二个中括号是第一个键值延伸的嵌套的字典类型键值;在等号后，先把原数据集按特征值分开，然后递归调用该函数
    return myTree#返回最终的字典信息

#使用决策树和标签来测试新样例的分类结果。  
def classify(inputTree,featLabels,testVec):#根据已有的决策树，对给出的数据进行分类
    firstStr = inputTree.keys()[0]
    secondDict = inputTree[firstStr]
    featIndex = featLabels.index(firstStr)#这里是将标签字符串转换成索引数字
    for key in secondDict.keys():
        if testVec[featIndex] == key:#如果key值等于给定的标签时
            if type(secondDict[key]).__name__ == 'dict':
                classLabel = classify(secondDict[key],featLabels,testVec)#递归调用分类
            else: classLabel = secondDict[key]#此数据的分类结果
    return classLabel



#使用pickle模块进行数据的序列化，调用dump()函数用于存放
def storeTree(inputTree,filename):
    import pickle
    fw = open(filename,'wb')
    print(type(fw))
    pickle.dump(inputTree,fw)

    fw.close()
    return "success"
#   调用load（）函数用于装载数据信息
def grabTree(filename):
    import pickle
    fr = open(filename,'rb')
    datatree=pickle.load(fr)
    return datatree
    
dataSet,labels=createDataSet()
labels1=labels[:]    #使用python的浅复制，在不同的内存中存储
shang=calcShannonEnt(dataSet)
print(shang)
mytree=createTree(dataSet,labels)  #label标签发生改变
print(mytree)
filename="mytree.txt"
print(storeTree(mytree,filename))
mytree0=grabTree(filename)
#调用分类函数，进行测试
x=input("请输入测试数据x")
y=input("请输入测试数据y")
data=[int(x), int(y)]
jieguo=classify(mytree,labels1,data)  
print(jieguo)    #输出结果


