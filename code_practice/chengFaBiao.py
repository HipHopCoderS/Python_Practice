# -*- coding:utf-8 -*-
__author__ = 'HipHopCoder'

#九九乘法表
#i  控制行数,j  控制相乘的个数



def chengFaBiao():

	for i in range(1,10):
		for j in range(1,i+1):
			print "%d*%d=%d"%(i,j,i*j),

		print "\n"




chengFaBiao()