# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2016-05-11 08:33:01
# @Last modified by:   WuLC
# @Last Modified time: 2016-05-11 08:34:05
# @Email: liangchaowu5@gmail.com

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        sum_ = reduce(lambda x,y:x*10+y,digits)
        return map(lambda x:int(x),str(sum_+1))