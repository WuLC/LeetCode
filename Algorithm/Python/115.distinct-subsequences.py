#
# @lc app=leetcode id=115 lang=python
#
# [115] Distinct Subsequences
#

# @lc code=start
class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        m, n = len(s), len(t)
        dp = [[0] * (n+1) for _ in range(m+1)]
        for i in range(m+1):
            dp[i][0] = 1

        for i in range(m):
            for j in range(n):
                if i < j:
                    continue
                dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j+1])
                if s[i] == t[j]:
                    dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j+1] + dp[i][j])
        return dp[m][n]
        
# @lc code=end

