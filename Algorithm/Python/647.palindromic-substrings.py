#
# @lc app=leetcode id=647 lang=python
#
# [647] Palindromic Substrings
#

# @lc code=start

from collections import defaultdict

class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        dp = [[0] * (n) for _ in range(n)]

        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and \
                   (i+1 >= j-1 or dp[i+1][j-1] == 1):
                        dp[i][j] = 1
        
        return sum(sum(dp[i]) for i in range(n))
                            
# @lc code=end

