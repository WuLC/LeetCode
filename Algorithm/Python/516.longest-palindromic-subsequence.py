#
# @lc app=leetcode id=516 lang=python
#
# [516] Longest Palindromic Subsequence
#

# @lc code=start
class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        result = 0
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if i == j:
                    dp[i][j] = 1
                elif s[i] == s[j]:
                    dp[i][j] = 2 
                    if i+1 <= j-1:
                        dp[i][j] += dp[i+1][j-1]
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i+1][j])
                    if i+1 <= j-1:
                        dp[i][j] = max(dp[i+1][j-1], dp[i][j])
                result = max(result, dp[i][j])
        return result
# @lc code=end

