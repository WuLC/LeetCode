# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2017-08-11 22:03:38
# @Last Modified by:   WuLC
# @Last Modified time: 2017-08-11 22:11:26


# dynamic programming
# dp[i] represents the number of Palindromic Substrings up until i(not necessarily include i)
class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        dp = [1 for _ in xrange(len(s))]
        indices = [[i, i+1] for i in xrange(len(s))] # i represents that s[i] is already a palindrome string while i + 1 is not
        for i in xrange(1, len(s)):
            dp[i] += dp[i-1]
            for index in indices[i-1]:
                if index - 1 >= 0 and s[index-1] == s[i]:
                    dp[i] += 1
                    indices[i].append(index-1)
        return dp[-1]