# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-08-22 09:13:55
# @Last modified by:   WuLC
# @Last Modified time: 2016-08-22 09:26:48
# @Email: liangchaowu5@gmail.com

# Dynamic Programming
# pay attention that some numbers are larger than the maximum product after seperating
class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0 for i in xrange(n+1)]
        dp[1] = 1
        for i in xrange(2,n+1):
            for j in xrange(1, i/2+1):
                dp[i] = max(dp[i], max(dp[j],j)*max(dp[i-j],i-j))
        return dp[n]
            
        