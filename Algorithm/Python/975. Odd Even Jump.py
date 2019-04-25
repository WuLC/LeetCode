# -*- coding: utf-8 -*-
# Created on Sat Apr 20 2019 17:6:26
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# dp, O(nlgn) time, O(n) space
# next greater/smaller element with stack

from collections import deque

class Solution(object):
    def oddEvenJumps(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n = len(A)
        sorted_A = sorted([(v, i) for i, v in enumerate(A)])
        next_greater, greater_stack = [-1] * n, []
        idx = n - 1
        while idx >= 0:
            while greater_stack and greater_stack[-1] < sorted_A[idx][1]:
                greater_stack.pop()
            if greater_stack:
                next_greater[sorted_A[idx][1]] = greater_stack[-1]
            greater_stack.append(sorted_A[idx][1])
            idx -= 1
        
        sorted_A = sorted([(v, -i) for i, v in enumerate(A)]) # -i if for repeated elements
        next_smaller, smaller_stack = [-1] * n, []
        idx = 0
        while idx < n:
            while smaller_stack and smaller_stack[-1] < -1*sorted_A[idx][1]:
                smaller_stack.pop()
            if smaller_stack:
                next_smaller[-1*sorted_A[idx][1]] = smaller_stack[-1]
            smaller_stack.append(-1*sorted_A[idx][1])
            idx += 1
        odd_dp, even_dp = [False] * n, [False] * n
        odd_dp[-1], even_dp[-1] = True, True
        result = 1
        for i in xrange(n - 2, -1, -1):
            if next_greater[i] >= 0 and even_dp[next_greater[i]]:
                odd_dp[i] = True
                result += 1
            if next_smaller[i] >= 0 and odd_dp[next_smaller[i]]:
                even_dp[i] = True
        return result