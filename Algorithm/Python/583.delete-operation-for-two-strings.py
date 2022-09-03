#
# @lc app=leetcode id=583 lang=python
#
# [583] Delete Operation for Two Strings
#

# @lc code=start


# same as longest common subsequence
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m, n = len(word1), len(word2)
        dp = [[0]*(n+1) for _ in range(m+1)]
        for i in range(m):
            for j in range(n):
                dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
                if word1[i] == word2[j]:
                    dp[i+1][j+1] = max(dp[i][j] + 1, dp[i+1][j+1])

        return m + n - 2*dp[m][n]

# same as longest common subsequence
# class Solution(object):
#     def minDistance(self, word1, word2):
#         """
#         :type word1: str
#         :type word2: str
#         :rtype: int
#         """
#         m, n = len(word1), len(word2)
#         dp = []
#         # init dp matrix
#         for i in range(m+1):
#             if i == 0:
#                 dp.append([1] * (n+1))
#                 dp[i][0] = 0
#             else:
#                 dp.append([0] * (n+1))
#                 dp[i][0] = 1
        
#         # iterate two words
#         for i in range(m):
#             for j in range(n):
#                 dp[i+1][j+1] = min(dp[i][j+1], dp[i+1][j]) + 1
#                 if word1[i] == word2[j]:
#                     dp[i+1][j+1] = min(dp[i+1][j+1], dp[i][j])
#         return dp[m][n]
        
# @lc code=end

