'''
时间复杂度：O(tkmn)，其中，t为迭代次数，k为中心的数目，m为数据量，n为数据维数；
空间复杂度：O((m+k)n)，其中，k为中心的数目，m为数据量，n为数据维数；
Pro: 速度快，原理简单，易于理解，剧累效果好
Con: 个数K 需要事先给定,却很难估计；不同初始化可能会导致不同结果；非凸函数不佳
Reference: https://blog.csdn.net/saltriver/article/details/76038467#:~:text=%E4%BA%8C%E3%80%81%E6%97%B6%E9%97%B4%E5%A4%8D%E6%9D%82%E5%BA%A6%E4%BB%8E,%E4%B8%BA%E6%95%B0%E6%8D%AE%E7%9A%84%E7%BB%B4%E6%95%B0%E3%80%82
https://cloud.tencent.com/developer/article/1604181
'''

import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

## calculate Euclidean distance
def calcDis(dataSet, centroids, k):
	clalist = []
	for data in dataSet:
		#相减   (np.tile(a,(2,1))就是把a先沿x轴复制1倍，即没有复制，仍然是 [0,1,2]。 再把结果沿y方向复制2倍得到array([[0,1,2],[0,1,2]]))
		diff = np.tile(data, (k, 1)) - centroids
		squaredDiff = diff ** 2     #平方
		squaredDist = np.sum(squaredDiff, axis=1)   #和  (axis=1表示行)
		distance = squaredDist ** 0.5 # 开根号
		clalist.append(distance)
	clalist = np.array(clalist) #返回一个每个点到质点的距离len(dateSet)*k的数组
	return clalist

# update centroids
def classify(dataSet, centroids, k):
	# 计算样本到质心的距离
	clalist = calcDis(dataSet, centroids, k)
	# 分组并计算新的质心
	minDistIndices = np.argmin(clalist, axis=1)   #axis=1 表示求出每行的最小值的下标
	#DataFramte(dataSet)对DataSet分组，groupby(min)按照min进行统计分类，mean()对分类结果求均值
	newCentroids = pd.DataFrame(dataSet).groupby(minDistIndices).mean()
	newCentroids = newCentroids.values
    # 计算变化量
	changed = newCentroids - centroids
	return changed, newCentroids

# main functions
def kmeans(dataSet, k):
	# 随机选取质心
	centroids = random.sample(dataSet, k)

	# 更新质心，知道变化量为0
	changed, newCentroids = classify(dataSet, centroids, k)
	while np.any(changed != 0):
		changed, newCentroids = classify(dataSet, newCentroids, k)
	centroids = sorted(newCentroids.tolist())   #tolist()将矩阵转换成列表 sorted()排序

	# 根据质心计算每个集群
	cluster = []
	clalist = calcDis(dataSet, centroids, k) # Euclidean distance
	minDistIndices = np.argmin(clalist, axis = 1)
	for i in range(k):
		cluster.append([])
	for i, j in enumerate(minDistIndices):
		cluster[j].append(dataSet[i])
	return centroids, cluster

# test with data
def createDataSet():
	return [[1,1], [1, 2], [2, 1], [6, 4], [6, 3], [5,4]]

if __name__=='__main__':
	dataSet = createDataSet()
	centroids, cluster = kmeans(dataSet, 2)
	print('centroids: %s' % centroids)
	print('clusters : %s' % cluster)
	for i in range(len(dataSet)):
		plt.scatter(dataSet[i][0], dataSet[i][1],
			marker = 'o', color = 'green', s = 40, label = 'data')
	for j in range(len(centroids)):
		plt.scatter(centroids[j][0], centroids[j][1],
			marker = 'x', color = 'red', s=50, label = 'centroids')
	plt.show()



