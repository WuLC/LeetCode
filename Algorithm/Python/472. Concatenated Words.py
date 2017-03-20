# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2017-03-21 00:50:47
# @Last modified by:   WuLC
# @Last Modified time: 2017-03-21 00:52:11
# @Email: liangchaowu5@gmail.com

# similar to 139.Word Break
# DP
class Solution(object):
    def findAllConcatenatedWordsInADict(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        words.sort()
        word_set = set(words)
        result = []
        for i in reversed(xrange(len(words))):
            if self.can_segment(word_set, words[i]):
                result.append(words[i])
            #word_set.remove(words[i])
        return result
            
    
    def can_segment(self, word_set, s):
        if len(s) == 0: return False # deal with empty string
        dp = [False for _ in xrange(len(s)+1)]
        dp[0] = True
        for i in xrange(len(s)):
            for j in xrange(i+1):
                if dp[j] and s[j:i+1] in word_set and (j!=0 or i!=len(s)-1):
                    dp[i+1] = True
                    break
        return dp[len(s)]