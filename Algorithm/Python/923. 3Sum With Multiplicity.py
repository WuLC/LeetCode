# -*- coding: utf-8 -*-
# Created on Thu Oct 25 2018 9:44:56
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# TLE， O(n^2) time complexity
from collections import defaultdict
class Solution(object):
    def threeSumMulti(self, A, target):
        """
        :type A: List[int]
        :type target: int
        :rtype: int
        """
        result = 0
        counter = defaultdict(int)
        for i in xrange(len(A)):
            result = (result + counter[target - A[i]]) % (1000000007)
            for j in xrange(i):
                counter[A[i] + A[j]] += 1
        return result