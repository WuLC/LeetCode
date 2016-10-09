# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2016-07-01 18:05:49
# @Last modified by:   WuLC
# @Last Modified time: 2016-07-01 18:06:00
# @Email: liangchaowu5@gmail.com

class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        tokens.append('0')
        tokens.append('+')
        stack, operand = [], None
        operators = ['+', '-', '*', '/']
        for i in xrange(len(tokens)):
            if tokens[i] in operators:
                p2 = stack.pop()
                p1 = stack.pop()
                if tokens[i] == '+':
                    operand = p1 + p2
                elif tokens[i] == '-':
                    operand = p1 - p2
                elif tokens[i] == '*':
                    operand = p1 * p2
                elif tokens[i] == '/':
                    operand = int(float(p1) / p2)
                stack.append(operand)
            else:
                stack.append(int(tokens[i]))
        return operand