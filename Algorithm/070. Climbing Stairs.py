# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-05-12 16:44:40
# @Last modified by:   WuLC
# @Last Modified time: 2016-05-12 16:44:57
# @Email: liangchaowu5@gmail.com

# DP 
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0 for i in xrange(n)]
        for i in xrange(n):
            if i==0:
                dp[i] = 1
            elif i==1:
                dp[i] = 2
            else:
                dp[i] = dp[i-1]+ dp[i-2]
        return dp[n-1]