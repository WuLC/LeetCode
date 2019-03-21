# -*- coding: utf-8 -*-
# Created on Wed Mar 20 2019 22:54:27
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# bit manipulation, pay attention to the case that N = 0

class Solution(object):
    def bitwiseComplement(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N == 0:
            return 1
        count, n = 0, N
        while n > 0:
            if n & 1 == 1:
                count += 1
            n >>= 1
        result, bit = 0, 0
        while count > 0:
            if N & 1 == 0:
                result += 2**bit
            else:
                count -= 1
            N >>= 1
            bit += 1
        return result
