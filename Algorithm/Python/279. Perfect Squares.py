# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-08-28 21:14:06
# @Last modified by:   WuLC
# @Last Modified time: 2016-08-28 22:10:10
# @Email: liangchaowu5@gmail.com

# normal DP, TLE
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [i for i in xrange(n+1)]
        for i in xrange(1, n+1):
            for j in xrange(1, int(i**0.5)+1):
                dp[i] = min(dp[i], dp[i-j*j]+1)
        return dp[n]


# static DP, AC
# since there are many test cases, keep the result of the previous test cases can be faster
class Solution(object):
    dp_ = [0, 1]
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = Solution.dp_
        if n<len(dp):
            return dp[n]
        for i in xrange(len(dp), n+1):
            dp.append(i)
            for j in xrange(1, int(i**0.5)+1):
                dp[i] = min(dp[i], dp[i-j*j]+1)
        return dp[n]
        