# -*- coding:utf-8 -*-
__author__ = 'HipHopCoder'


#键盘获取输入的两个数,算出两个数的和差积商


def NumAdd():

	a = int(raw_input("请输入一个数字"))
	b = int(raw_input("请输入另一个数字"))

	print "两个数字的和为:%d+%d=%d"%(a,b,a+b)
	print "两个数字的差为:%d-%d=%d"%(a,b,a-b)
	print "两个数字的积为:%d*%d=%d"%(a,b,a*b)
	print "两个数字的商为:%d+%d=%d"%(a,b,a/b)



NumAdd()