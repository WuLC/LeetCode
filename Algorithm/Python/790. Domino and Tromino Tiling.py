# -*- coding: utf-8 -*-
# Created on Fri Mar 23 2018 14:31:58
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# dp,O(n) time, O(n) space
# referer: https://leetcode.com/problems/domino-and-tromino-tiling/discuss/116664/Schematic-explanation-of-two-equivalent-DP-recurrence-formula

class Solution(object):    
    def __init__(self):
        self.dp = [1, 1, 2]
        
    def numTilings(self, N):
        """
        :type N: int
        :rtype: int
        """
        for i in xrange(len(self.dp), N+1):
            self.dp.append((2*self.dp[i-1] + self.dp[i-3])%1000000007)
        return self.dp[N]