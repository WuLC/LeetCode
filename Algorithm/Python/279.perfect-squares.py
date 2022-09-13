#
# @lc app=leetcode id=279 lang=python
#
# [279] Perfect Squares
#

# @lc code=start

import math

class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [i for i in range(n+1)]
        for i in range(1, int(math.sqrt(n))+1):
            for j in range(i**2, n+1):
                dp[j] = min(dp[j], dp[j - i**2] + 1)
        return dp[n]
        
# @lc code=end

