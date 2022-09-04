#
# @lc app=leetcode id=72 lang=python
#
# [72] Edit Distance
#

# @lc code=start
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m, n = len(word1), len(word2)

        dp = []
        for i in range(m+1):
            if i == 0:
                dp.append([j for j in range(n+1)])
            else:
                dp.append([0]*(n+1))
                dp[i][0] = i

        for i in range(m):
            for j in range(n):
                #[delete, replace, insert]
                op = [dp[i][j+1], dp[i][j], dp[i+1][j]] 
                dp[i+1][j+1] = min(op) + 1
                if word1[i] == word2[j]:
                    dp[i+1][j+1] = min(dp[i][j], dp[i+1][j+1])
        return dp[m][n]
# @lc code=end

