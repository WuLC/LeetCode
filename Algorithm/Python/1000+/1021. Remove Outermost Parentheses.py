# -*- coding: utf-8 -*-
# Created on Tue Apr 09 2019 10:42:53
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# stack
class Solution(object):
    def removeOuterParentheses(self, S):
        """
        :type S: str
        :rtype: str
        """
        result, stack = "", []
        for i in xrange(len(S)):
            if S[i] == '(':
                stack.append(i)
            else:
                idx = stack.pop()
                if len(stack) == 0:
                    result += S[idx+1:i]
        return result