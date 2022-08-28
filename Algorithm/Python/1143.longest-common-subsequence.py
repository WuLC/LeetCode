#
# @lc app=leetcode id=1143 lang=python
#
# [1143] Longest Common Subsequence
#

# @lc code=start
class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        m, n = len(text1), len(text2)
        result = 0
        dp = [[0]*(n+1) for _ in range(m+1)]
        for i in range(m):
            for j in range(n):
                dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])
                if text1[i] == text2[j]:
                    dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j] + 1)
                result = max(dp[i+1][j+1], result)
        return result
        
# @lc code=end

