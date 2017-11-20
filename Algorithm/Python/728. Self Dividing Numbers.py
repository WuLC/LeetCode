# -*- coding: utf-8 -*-
# Created on Mon Nov 20 2017 9:20:28
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# easy solution

class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        result = []
        for num in xrange(left, right+1):
            legal = True
            for digit in str(num):
                if digit == '0' or num % int(digit) != 0:
                    legal = False
                    break
            if legal:
                result.append(num)
        return result
        