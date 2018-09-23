# -*- coding: utf-8 -*-
# Created on Sun Sep 23 2018 11:57:30
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# simple solution
class Solution(object):
    def smallestRangeI(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        diff = max(A) - min(A)
        return 0 if diff<=K*2 else diff-K*2