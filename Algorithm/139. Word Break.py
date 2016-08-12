# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-08-12 08:59:46
# @Last modified by:   WuLC
# @Last Modified time: 2016-08-12 09:34:57
# @Email: liangchaowu5@gmail.com

# method 1, backtracking, TLE
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        return self.helper(0, s, wordDict)
        
    def helper(self, index, s, wordDict):
        if index == len(s):
            return True
        tmp = ''
        while index < len(s):
            tmp += s[index]
            index += 1
            if tmp in wordDict:
                if self.helper(index, s, wordDict):
                    return True
        return False

# method 2, DP
# dp[i] represents the whether s[:i] can be segmented
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        dp = [False for i in xrange(len(s))]
        dp.insert(0, True)
        for i in xrange(1, len(s)+1):
            for j in xrange(1,i+1): # a little faster in average case: for j in reversed(xrange(1,i+1)):
                if dp[j-1] and s[j-1:i] in wordDict:
                    dp[i] = True
                    break
        return dp[len(s)]