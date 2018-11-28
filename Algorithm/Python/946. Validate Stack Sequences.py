# -*- coding: utf-8 -*-
# Created on Wed Nov 28 2018 9:19:19
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# two pointers
# for each element in popped, check it whether is in the top of the current stack, the check it in the later part of pushed
class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        stack = []
        p1, p2 = 0, 0
        while p1 < len(pushed) and p2 <= popped:
            if pushed[p1] == popped[p2]:
                p1, p2 = p1 + 1, p2 + 1
            elif stack and stack[-1] == popped[p2]:
                stack.pop()
                p2 += 1
            else:
                while p1 < len(pushed) and pushed[p1] != popped[p2]:
                    stack.append(pushed[p1])
                    p1 += 1
        while p2 < len(popped) and stack and popped[p2] == stack[-1]:
            p2 += 1
            stack.pop()
        return p2 == len(popped)