# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-05-16 11:18:26
# @Last modified by:   WuLC
# @Last Modified time: 2016-05-16 11:19:06
# @Email: liangchaowu5@gmail.com
# Referer:http://www.stanford.edu/class/cs124/lec/med.pdf

# DP 
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        # init the dp matrix
        m = len(word1)
        n = len(word2)
        dp = [[0 for i in xrange(n+1)] for j in xrange(m+1)]
        for j in xrange(n+1):
            dp[0][j] = j
        for i in xrange(m+1):
            dp[i][0] = i
        # transver the matrix,left-->right and up-->down
        for i in xrange(1,m+1):
            for j in xrange(1,n+1):
                inse = dp[i][j-1] + 1
                dele = dp[i-1][j] + 1
                if word1[i-1] == word2[j-1]:
                    repl = dp[i-1][j-1]
                else:
                    repl = dp[i-1][j-1] + 1
                dp[i][j] = min(inse,dele,repl)
        return dp[m][n]
        
                    
                
        