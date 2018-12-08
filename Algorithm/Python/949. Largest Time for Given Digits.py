# -*- coding: utf-8 -*-
# Created on Sun Dec 02 2018 18:56:55
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# permutation
from itertools import permutations
class Solution(object):
    def largestTimeFromDigits(self, A):
        """
        :type A: List[int]
        :rtype: str
        """
        candidate = ["{0}{1}:{2}{3}".format(*t) for t in permutations(A) if t[0] * 10 + t[1] < 24 and t[2] < 6]
        return "" if len(candidate) == 0 else max(candidate)
