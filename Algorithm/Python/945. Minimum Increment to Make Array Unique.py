# -*- coding: utf-8 -*-
# Created on Mon Nov 26 2018 21:22:45
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# greedy
# keep idx as current position to hold the next number
from collections import Counter
class Solution(object):
    def minIncrementForUnique(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A) == 0:
            return 0
        count = sorted(Counter(A))
        idx = count[0][0]
        result = 0
        for k, v in count:
            if idx <= k:
                result += ((v - 1) * v) / 2
                idx = k + v
            else:
                result += (idx - k) * v + ((v - 1) * v) / 2
                idx += v
        return result