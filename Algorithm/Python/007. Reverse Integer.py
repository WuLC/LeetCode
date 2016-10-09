# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2016-02-07 09:51:59
# @Last modified by:   LC
# @Last Modified time: 2016-04-10 16:24:00
# @Email: liangchaowu5@gmail.com

##############################
#将int类型转换成str类型，将str类型反转即可
#如果采用取模方法首先难以确定整数的位数，再者有溢出的可能
##############################

class Solution(object):
    def  reverse(self,x):
        """
        type x : int
        rtype : int
        """
        flag=1
        if x<0:
            flag=-1
            x*=flag
        strX=str(x)
        x=strX[::-1]
        result=int(x)
        if result > math.pow(2, 31): #处理溢出问题，整数有32个bit
            return 0
        else:
            return result*flag