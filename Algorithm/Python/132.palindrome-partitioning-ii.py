#
# @lc app=leetcode id=132 lang=python
#
# [132] Palindrome Partitioning II
#

# @lc code=start
class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        # use dp instead of backtrack, compared with 131
        n = len(s)
        is_palidormine = [[False]*n for _ in range(n)]
        for i in range(n-1, -1, -1):
            for j in range(i, n, 1):
                if i == j:
                    is_palidormine[i][j] = True
                elif s[i] == s[j] and (i+1 >= j-1 or is_palidormine[i+1][j-1]):
                    is_palidormine[i][j] = True
        
        dp = [i for i in range(n)]
        for i in range(1, n):
            for j in range(i+1):
                if is_palidormine[j][i]:
                    dp[i] = 0 if j == 0 else min(dp[i], dp[j-1]+1)
        return dp[-1]

# @lc code=end

