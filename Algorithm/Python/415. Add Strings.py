# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2016-10-15 00:34:49
# @Last modified by:   WuLC
# @Last Modified time: 2016-10-15 00:35:28
# @Email: liangchaowu5@gmail.com

# add digit by digit, pay attention to carry
class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        p1, p2 = len(num1)-1, len(num2)-1
        carry = 0
        result = ''
        while p1 >= 0 or p2 >= 0:
            total = carry
            if p1 >= 0:
                total += int(num1[p1])
                p1 -= 1
            if p2 >= 0:
                total += int(num2[p2])
                p2 -= 1
            carry, remainder = divmod(total, 10)
            result = str(remainder) + result
        if carry:
            result = str(carry) + result
        return result
            