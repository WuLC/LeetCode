# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2017-08-13 08:44:30
# @Last Modified by:   WuLC
# @Last Modified time: 2017-08-13 09:02:51

# two kinds of dp

# first kind of dp: dp[i] represents the maximum length of pair chain that ends with dp[i]
# time: O(n^2), TLE
class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        pairs.sort(cmp = lambda a, b : a[0]-b[0])
        dp = [1 for _ in xrange(len(pairs))]
        result = 0
        for i in xrange(len(pairs)):
            for j in xrange(i):
                if pairs[i][0] > pairs[j][1]:
                    dp[i] = max(dp[i], dp[j] + 1)
            result = max(result, dp[i])
        return result

# second kind of dp: dp[i] represents the maximum length of pair chain up until dp[i](not necessarily include pairs[i])
# average time complexity: O(n^2), but faster than the first dp, AC
class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        pairs.sort(cmp = lambda a, b : a[0]-b[0])
        dp = [1 for _ in xrange(len(pairs))]
        for i in xrange(len(pairs)):
            for j in reversed(xrange(i)):
                if pairs[i][0] > pairs[j][1]:
                    dp[i] = dp[j] + 1
                    break
        return dp[-1] if len(dp) > 0 else 0
                    
        
