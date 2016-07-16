# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2016-07-16 13:08:21
# @Last modified by:   WuLC
# @Last Modified time: 2016-07-16 22:45:39
# @Email: liangchaowu5@gmail.com


# check whether remainder  has ever appear through calculating  bit after bit
class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        stack = []
        r, m = divmod(abs(numerator), abs(denominator))
        sign = '-' if numerator * denominator < 0 else ''
        result = [sign + str(r), '.']
        while m not in stack and m != 0:
            stack.append(m)
            r, m = divmod(m*10, abs(denominator))
            result.append(str(r))
        if m != 0:
            idx = stack.index(m)
            result.insert(idx+2, '(')
            result.append(')')
            return ''.join(result)
        else:
            return ''.join(result).rstrip('.')