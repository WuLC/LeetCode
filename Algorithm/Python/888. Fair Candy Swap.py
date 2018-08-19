# -*- coding: utf-8 -*-
# Created on Sun Aug 19 2018 10:27:11
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# simple solution
class Solution(object):
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        diff = (sum(B) - sum(A))/2
        sA = set(A)
        for num in B:
            if num-diff in sA:
                return [num-diff, num]
                