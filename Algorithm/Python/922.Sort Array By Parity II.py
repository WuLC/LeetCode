# -*- coding: utf-8 -*-
# Created on Tue Oct 23 2018 9:53:30
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# two pointers
class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        odd_idx, even_idx = 1, 0
        n = len(A)
        while odd_idx < n  and even_idx < n:
          while odd_idx < n and (A[odd_idx]&1) != 0:
            odd_idx += 2
          while even_idx < n and (A[even_idx]&1) == 0:
            even_idx += 2
          if odd_idx < n and even_idx < n:
            A[odd_idx], A[even_idx] = A[even_idx], A[odd_idx]
            odd_idx += 2
            even_idx += 2
        return A