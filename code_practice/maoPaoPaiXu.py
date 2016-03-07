# -*- coding:utf-8 -*-
__author__ = 'HipHopCoder'

# 冒泡排序求最大值
def MaxMaoPao1(listTest):

	lenList = len(listTest)

	while lenList >0:
		for i in range(lenList-1):
			if listTest[i]>listTest[i+1]:
				listTest[i] = listTest[i] + listTest[i+1]
				listTest[i+1] = listTest[i] - listTest[i+1]
				listTest[i] = listTest[i] - listTest[i+1]

		lenList -= 1

	print listTest



# 冒泡排序求最大值
# i 控制比较的数字
# j 控制比较的位置
# 外层for  控制每个数的循环
# 内层for 控制每次的循环
def MaxMaoPao2(listTest):

	lenList = len(listTest)

	for i in range(lenList-1):
		for j in range(lenList-i):
			if listTest[i] > listTest[i+1]:
				value = listTest[i+1]
				listTest[i+1] = listTest[i]
				listTest[i] = value


	print listTest





listTest = [11,33,22,44,76,4,77]

MaxMaoPao1(listTest)
MaxMaoPao2(listTest)