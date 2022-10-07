#
# @lc app=leetcode id=647 lang=python
#
# [647] Palindromic Substrings
#

# @lc code=start
class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        result, n = 0, len(s)
        dp = [[False]*n for _ in range(n)]
        for i in range(n-1, -1, -1):
            for j in range(i, n, 1):
                if s[i] == s[j] and (i+1 >= j-1 or dp[i+1][j-1]):
                    dp[i][j] = True
                    result += 1
        return result
        
# @lc code=end

