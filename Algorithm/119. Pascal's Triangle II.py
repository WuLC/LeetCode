# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2016-06-18 23:58:03
# @Last modified by:   LC
# @Last Modified time: 2016-06-18 23:58:10
# @Email: liangchaowu5@gmail.com

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        result = [1]
        for i in xrange(rowIndex):
            for j in xrange(len(result)-1):
                result[j] += result[j+1]
            result[len(result)-1] = 1
            result.insert(0, 1)
        return result