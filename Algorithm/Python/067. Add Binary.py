# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2016-05-11 09:17:43
# @Last modified by:   WuLC
# @Last Modified time: 2016-05-11 09:18:06
# @Email: liangchaowu5@gmail.com

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        sum_ = self.binary2int(a)+self.binary2int(b)
        return self.int2binary(sum_)
    
        
    def binary2int(self,s):
        if len(s) == 1:
            return int(s)
        return reduce(lambda x,y:int(x)*2 + int(y),s)
    

    def int2binary(self,num):
        if num == 0:
            return '0'
        result = []
        while num!=0:
            num, tmp = divmod(num,2)
            result.insert(0,tmp)
        return reduce(lambda x,y:str(x)+str(y),result)
        
        