# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2016-08-31 14:08:47
# @Last modified by:   WuLC
# @Last Modified time: 2016-09-01 15:10:38
# @Email: liangchaowu5@gmail.com

# binary search is wrong, for example: when n = 4, binary search will get 5, but actually 4 is enough

# top-bottom DP 
class Solution(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [[0]*(n+1) for i in xrange(n+1)]
        return self.helper(dp, 1, n)
         
        
    def helper(self, dp, s, e):
        if s>=e:
            return 0
        if dp[s][e] != 0: # require, otherwise TLE
            return dp[s][e]
        tmp = None
        for i in xrange(s,e):
            left, right = self.helper(dp, s, i-1), self.helper(dp, i+1, e)
            if tmp:
                tmp = min(tmp, i + max(left, right))
            else:
                tmp = i + max(left,right)
        if tmp: dp[s][e] = tmp
        return dp[s][e]
             
