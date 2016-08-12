# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-08-12 10:15:58
# @Last modified by:   WuLC
# @Last Modified time: 2016-08-12 14:40:25
# @Email: liangchaowu5@gmail.com

# method 1, DP, MLE
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]
        """
        dp = [[] for i in xrange(len(s)+1)]
        for i in xrange(1, len(s)+1):
            for j in xrange(1, i+1):
                tmp = s[j-1:i]
                if (j == 1 or dp[j-1]) and tmp in wordDict:
                    if j==1:
                        dp[i].append(tmp)
                    else:
                        for sep in dp[j-1]:
                            dp[i].append(sep+' '+tmp)
        return dp[len(s)]
          


# method 2, backtracking, TLE
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]
        """
        result = []
        for i in xrange(1,len(s)+1):
            tmp = s[:i]
            if tmp in wordDict:
                if i==len(s):
                    result.append(tmp)
                else:
                    words = self.wordBreak(s[i:], wordDict)
                    for word in words:
                        result.append(tmp+' '+word)
        return result
                

# method 3, based on method  2 
# add cache to it 
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]
        """
        return self.helper(s, wordDict, {})
        
    def helper(self, s, wordDict, cache):
        if s in cache:
            return cache[s]
        result = []
        for i in xrange(1,len(s)+1):
            tmp = s[:i]
            if tmp in wordDict:
                if i==len(s):
                    result.append(tmp)
                else:
                    words = self.helper(s[i:], wordDict, cache)
                    for word in words:
                        result.append(tmp+' '+word)
        cache[s] = result
        return result