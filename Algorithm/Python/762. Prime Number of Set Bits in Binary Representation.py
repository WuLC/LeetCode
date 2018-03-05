# -*- coding: utf-8 -*-
# Created on Tue Jan 30 2018 22:35:11
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# bit manipulation 
# the most important thing is pay attention to the range of L and R, so as to find all possible primes previously
class Solution(object):
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        primes = {2, 3, 5, 7, 11, 13, 17, 19}
        prime_count = 0
        for num in xrange(L, R+1):
            bit_count = 0
            while num > 0:
                bit_count += (num&1)
                num >>= 1
            if bit_count in primes:
                prime_count += 1
        return prime_count
                