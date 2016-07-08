# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-07-08 19:00:49
# @Last modified by:   WuLC
# @Last Modified time: 2016-07-08 19:00:59
# @Email: liangchaowu5@gmail.com

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result, pre_level= [], []
        for i in xrange(numRows):
            if i == 0:
                result.append([1])
            elif i == 1:
                result.append([1, 1])
                pre_level = [1, 1]
            else:
                tmp = [1]
                for j in xrange(len(pre_level)-1):
                    tmp.append(pre_level[j] + pre_level[j+1])
                tmp.append(1)
                pre_level = tmp 
                result.append(tmp)
        return result