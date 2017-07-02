# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2017-07-02 16:42:06
# @Last Modified by:   WuLC
# @Last Modified time: 2017-07-02 16:44:19


# dp, dp[n] = (n-1) * (dp[n-1] + dp[n-2])
# referer: http://www.geeksforgeeks.org/count-derangements-permutation-such-that-no-element-appears-in-its-original-position/
class Solution(object):
    def findDerangement(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 0
        elif n == 2:
            return 1
        else:
            pre1, pre2 = 0, 1
            for i in xrange(3, n+1):
                tmp = (i-1)*(pre1 + pre2) % 1000000007
                pre1, pre2 = pre2, tmp
            return pre2