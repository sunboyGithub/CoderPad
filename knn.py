'''
Time  C:  O(mn+mlogm)，其中，k，m为数据量，n为数据维数；
Space C:  O(mn)
Pro: 简单、有效。 训练的代价较低, 比较适用于样本容量比较大的类域的自动分类
Con: 懒散学习方法(lazy learning), 而一些积极学习的算法要快很多。需要存储全部的训练样本。可解释性不强。计算量较大。
Reference: https://cloud.tencent.com/developer/article/1604180
'''
import numpy as np
import operator
dataSet = np.array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
labels = ['A', 'A', 'B', 'B']
def classify0(inX, dataSet, labels, k):
    # 求出样本集的行数，也就是labels 标签的数目
    dataSetSize = dataSet.shape[0]

    # 构造输入值和样本集的差值矩阵
    diffMat = np.tile(inX, (dataSetSize, 1)) - dataSet

    # Cal Eudicean distance
    sqDiffMat = diffMat**2
    sqDistances = sqDiffMat.sum(axis = 1)
    distances = sqDistances**0.5

    # get ranking index
    sortedDistIndicies = distances.argsort()

    # get labels of most cloest k points
    classCount = {}
    for i in range(k):
        # 取第 i+1 邻近的样本对应的类别标签
        voteIlabel = labels[sortedDistIndicies[i]]
        # 以标签为key, 标签出现的次数为 value, 将统计到的标签及出现的次数写进字典
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1

    # 对字典按value从大到小排序
    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)

    # 返回排序后字典最大的value对应的key
    return sortedClassCount[0][0]
if __name__ == '__main__':
    print(classify0([1.1, 0], dataSet, labels, 3))