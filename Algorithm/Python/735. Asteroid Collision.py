# -*- coding: utf-8 -*-
# Created on Sun Nov 26 2017 11:43:0
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# stack
# pay attention that all the numbers in the stack are always of the same sign except that
# the left part are nagative and the right part are positive

class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack = []
        for aster in asteroids:
            if len(stack) == 0 or stack[-1] * aster > 0 or (stack[-1] < 0 and aster > 0):
                stack.append(aster)
            elif abs(stack[-1]) > abs(aster):
                    continue
            elif abs(stack[-1]) == abs(aster):
                stack.pop()
            else:
                while stack and stack[-1]*aster < 0 and abs(stack[-1]) < abs(aster):
                    stack.pop()
                if len(stack) == 0 or stack[-1]*aster > 0:
                    stack.append(aster)
                elif abs(stack[-1]) == abs(aster):
                    stack.pop()
        return stack