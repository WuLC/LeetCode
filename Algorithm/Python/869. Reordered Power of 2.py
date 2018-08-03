# -*- coding: utf-8 -*-
# Created on Fri Aug 03 2018 9:3:4
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# iterate all possible candidates the have the same length of N
from collections import Counter
class Solution(object):
    def reorderedPowerOf2(self, N):
        """
        :type N: int
        :rtype: bool
        """
        n = len(str(N))
        original = Counter(str(N))
        exp = int(math.log(10**(n-1), 2))
        candidate = str(2**exp)
        while len(candidate)<=n:
            if Counter(candidate) == original:
                return True
            exp += 1
            candidate = str(2**exp)
        return False
                  