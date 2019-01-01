# -*- coding: utf-8 -*-
# Created on Sat Dec 29 2018 16:27:48
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# order of the array has nothing to do with the result
# calculate the contribution of each element to the final result and add them up
# use 1<<i instead of 2**i to avoid overflow
class Solution(object):
    def sumSubseqWidths(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        MOD = 1000000007
        n = len(A)
        A.sort()
        return sum((((1 << i) - (1 << (n-i-1))) * A[i]) % MOD for i in xrange(n)) % MOD