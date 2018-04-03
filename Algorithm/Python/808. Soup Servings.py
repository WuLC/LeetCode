# -*- coding: utf-8 -*-
# Created on Tue Apr 03 2018 9:32:56
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# dp for probability problem
# use cache to avoid TLE, when N > 4800, just return 1
# reference: https://leetcode.com/problems/soup-servings/discuss/121711/C++JavaPython-When-N-greater-4800-just-return-1
import math
class Solution(object):
    def __init__(self):
        self.cache = {}
    
    def soupServings(self, N):
        """
        :type N: int
        :rtype: float
        """
        if N > 4800:
            return 1
        N = math.ceil(N/25.0)
        return self.helper(N, N)
    
    def helper(self, a, b):
        if a <= 0 and b <= 0:
            return 0.5
        elif a<= 0:
            return 1
        elif b <= 0:
            return 0
        if (a,b) not in self.cache:
            self.cache[(a,b)] =0.25*(self.helper(a-4, b) + self.helper(a-3, b-1) + self.helper(a-2, b-2) + self.helper(a-1, b-3))
        return self.cache[(a,b)]