# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2016-05-29 11:28:19
# @Last modified by:   WuLC
# @Last Modified time: 2016-05-29 11:29:04
# @Email: liangchaowu5@gmail.com


# DP, be careful that 0 can't be decode to any character
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if n == 0 or s[0] == '0':
            return 0
        dp = [1 for i in xrange(n+1)]
        
        for i in xrange(1, n):
            if s[i] == '0':
                if 0 < int(s[i-1]+s[i]) <= 26:
                    dp[i+1] = dp[i-1]
                else:
                    return 0
            else:
                if 0 < int(s[i-1]+s[i]) <= 26 and s[i-1] != '0':
                    dp[i+1] = dp[i-1] + dp[i]
                else:
                    dp[i+1] = dp[i]
        return dp[n]
                
            