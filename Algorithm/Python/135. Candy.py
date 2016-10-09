# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2016-07-17 10:23:29
# @Last modified by:   WuLC
# @Last Modified time: 2016-07-17 10:23:37
# @Email: liangchaowu5@gmail.com

class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        result = [1 for i in xrange(len(ratings))]
        for i in xrange(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                result[i] = result[i-1] + 1
        for i in xrange(len(ratings)-2, -1, -1): # or for i in reversed(xrange(0,len(ratings)-1))
            if ratings[i] > ratings[i+1]:
                result[i] = max(result[i], result[i+1]+1)
        return sum(result)