# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2016-07-18 10:13:32
# @Last modified by:   WuLC
# @Last Modified time: 2016-07-18 16:26:30
# @Email: liangchaowu5@gmail.com

# backtracking, TLE
class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0: return 0
        result = []
        self.helper(s, 0, -1, result)
        return min(result)
        
    def helper(self, s, idx, count, result):
        if idx == len(s):
            result.append(count)
            return
        for i in xrange(idx+1, len(s)+1):
            t = s[idx:i]
            if self.is_palindrome(t):
                self.helper(s, i, count + 1, result)
            
    def is_palindrome(self, s):
        n = len(s)
        for i in xrange(n/2):
            if s[i] != s[n-i-1]:
                return False
        return True

# DP1, TLE
class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = [0 for i in xrange(len(s))]
        for i in xrange(1, len(s)):
            min_cut = None
            for j in xrange(i+1):
                if self.is_palindrome(s[j:i+1]):
                    if min_cut == None:
                        if j == 0:
                            min_cut = 0
                            break
                        else:
                            min_cut = dp[j-1]+1 
                    else:
                        min_cut = min(min_cut, dp[j-1]+1)
            print dp[i]
        return dp[len(s)-1]
                
            
    def is_palindrome(self, s):
        n = len(s)
        for i in xrange(n/2):
            if s[i] != s[n-i-1]:
                return False
        return True