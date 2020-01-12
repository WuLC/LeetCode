# -*- coding: utf-8 -*-
# Created on Sun Jan 12 2020 15:30:54
# Author: WuLC
# EMail: liangchaowu5@gmail.com

class Solution(object):
    def minFlips(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        result = 0
        while a or b or c:
            last_bit = c&1;
            if last_bit == 1 and ((a&1)|(b&1)) == 0:
                result += 1
            elif last_bit == 0 and ((a&1)|(b&1)) == 1:
                result += (a&1) + (b&1)
            a >>= 1
            b >>= 1
            c >>= 1
        return result
                
        