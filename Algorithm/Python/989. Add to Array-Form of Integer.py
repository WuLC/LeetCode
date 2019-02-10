# -*- coding: utf-8 -*-
# Created on Sun Feb 10 2019 10:36:45
# Author: WuLC
# EMail: liangchaowu5@gmail.com

from collections import deque

class Solution(object):
    def addToArrayForm(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: List[int]
        """
        result = deque()
        str_K = str(K)
        i, j, carry = len(A) - 1, len(str_K - 1), 0
        while i >= 0 or j >= 0:        
            if i >= 0 and j >= 0:
                tmp = A[i] + int(str_K[j]) + carry
            elif i >= 0:
                tmp = A[i] + carry
            elif j >= 0:
                tmp = int(str_K[j]) + carry
            carry, curr = tmp/10, tmp%10
            result.appendleft(curr)
            i -= 1
            j -= 1
        if carry:
            result.appendleft(carry)
        return list(result)