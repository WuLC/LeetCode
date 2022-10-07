#
# @lc app=leetcode id=5 lang=python
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        result, n = "", len(s)
        dp = [[False]*n for _ in range(n)]
        for i in range(n-1, -1, -1):
            for j in range(i, n, 1):
                if i == j:
                    dp[i][j] = True
                elif s[i] == s[j] and (i+1 >= j-1 or dp[i+1][j-1]):
                    dp[i][j] = True

                if dp[i][j] and j-i+1 > len(result):
                    result = s[i:j+1]
        return result

# @lc code=end

