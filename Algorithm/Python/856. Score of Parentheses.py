# -*- coding: utf-8 -*-
# Created on Sun Aug 19 2018 12:51:34
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# stack
class Solution(object):
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        stack = []
        for i in xrange(len(S)):
            if S[i] == '(':
                stack.append(S[i])
            else:
                curr = 0
                tmp = stack.pop()
                while tmp != '(':
                    curr += tmp
                    tmp = stack.pop()
                if curr==0:
                    stack.append(1)
                else:
                    stack.append(curr*2)
        return sum(stack)