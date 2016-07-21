# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-07-21 10:23:33
# @Last modified by:   WuLC
# @Last Modified time: 2016-07-21 10:23:49
# @Email: liangchaowu5@gmail.com

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        return sum([max(prices[i]-prices[i-1], 0) for i in xrange(1,len(prices)) ])