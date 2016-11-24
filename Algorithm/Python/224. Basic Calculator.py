# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-11-24 13:07:08
# @Last modified by:   WuLC
# @Last Modified time: 2016-11-24 13:13:13
# @Email: liangchaowu5@gmail.com



# take the plus or minus as the sign of the number following it, then just add all numbers
# use stack to store previous result when meeting '('
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        result, sign = 0, 1
        stack = []
        i = 0
        while i < len(s):
            if s[i].isdigit():
                tmp = s[i]
                while i+1 < len(s) and s[i+1].isdigit():
                    i += 1
                    tmp += s[i]
                result += sign * int(tmp)
            elif s[i] == '+':
                sign = 1
            elif s[i] == '-':
                sign = -1
            elif s[i] == '(':
                stack.append(result)
                stack.append(sign)
                result = 0
                sign = 1
            elif s[i] == ')':
                result = result*stack.pop() + stack.pop()
            i += 1
        return result