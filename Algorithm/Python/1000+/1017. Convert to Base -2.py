# -*- coding: utf-8 -*-
# Created on Wed Apr 03 2019 7:36:4
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# bit manipulation
class Solution(object):
    def baseNeg2(self, N):
        """
        :type N: int
        :rtype: str
        """
        if N == 0:
            return "0"
        result = ""
        idx, carry = 0, 0
        while N or carry:
            s = (N&1) + carry
            curr, carry = s % 2, s / 2
            result = str(curr) + result
            if (idx&1) and curr:
                carry = 1
            N >>= 1
            idx += 1
        return result