# -*- coding: utf-8 -*-
# Created on Mon Jul 17 2018 15:35:57
# Author: WuLC
# EMail: liangchaowu5@gmail.com

class Solution(object):
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        result = 0
        pre, curr = -1, 0
        while N:
            if (N&1) == 1:
                if pre != -1:
                    result = max(result, curr - pre)
                pre = curr
            curr += 1
            N >>= 1
        return result
                