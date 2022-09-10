#
# @lc app=leetcode id=1049 lang=python
#
# [1049] Last Stone Weight II
#

# @lc code=start
class Solution(object):
    def lastStoneWeightII(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        m, n = len(stones), sum(stones)>>1
        dp = [[0]*(n+1) for _ in range(m+1)]
        for i in range(m):
            for j in range(n+1):
                dp[i+1][j] = dp[i][j]
                if j >= stones[i]:
                    dp[i+1][j] = max(dp[i+1][j], dp[i][j-stones[i]] + stones[i])
        
        return sum(stones) - dp[m][n] - dp[m][n]
        
# @lc code=end

