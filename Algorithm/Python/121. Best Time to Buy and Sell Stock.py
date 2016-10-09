# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2016-07-12 09:16:33
# @Last modified by:   WuLC
# @Last Modified time: 2016-07-12 09:16:48
# @Email: liangchaowu5@gmail.com

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_val, max_val= [], []
        curr_min, curr_max, result = None, None, 0
        for i in xrange(len(prices)):
            curr_min = min(curr_min, prices[i]) if curr_min else prices[i]
            min_val.append(curr_min)
        for i in reversed(xrange(len(prices))):
            curr_max = max(curr_max, prices[i]) if curr_max else prices[i]
            max_val.append(curr_max)
        max_val.reverse()
        for i in xrange(len(prices)):
            result = max(result, max_val[i]-min_val[i])
        return result