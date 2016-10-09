# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-07-04 22:56:00
# @Last modified by:   WuLC
# @Last Modified time: 2016-07-04 22:56:24
# @Email: liangchaowu5@gmail.com

class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if (len(s1)+len(s2)) != len(s3):
            return False
        dp = [[ False for j in xrange(len(s2)+1)] for i in xrange(len(s1)+1)]
        for i in xrange(len(s1)+1):
            for j in xrange(len(s2)+1):
                if i==0 and j==0:
                    dp[i][j] = True
                elif i == 0:
                    dp[i][j] = dp[i][j-1] and s2[j-1] == s3[i+j-1]
                elif j == 0:
                    dp[i][j] = dp[i-1][j] and s1[i-1] == s3[i+j-1]
                else:
                    dp[i][j] = (dp[i][j-1] and s2[j-1] == s3[i+j-1]) or (dp[i-1][j] and s1[i-1] == s3[i+j-1])
        return dp[len(s1)][len(s2)]