# -*- coding: utf-8 -*-
# Created on Sun Feb 10 2019 11:20:4
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# chang Y to X
# greedy: when Y is odd, perform Y-1, else perform Y/2
class Solution(object):
    def brokenCalc(self, X, Y):
        """
        :type X: int
        :type Y: int
        :rtype: int
        """
        if X >= Y:
            return X - Y
        return 1+self.brokenCalc(X, Y+1) if (Y&1) == 1 else 1+self.brokenCalc(X, Y>>1)