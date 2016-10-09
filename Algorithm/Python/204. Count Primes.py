# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-07-30 23:07:18
# @Last modified by:   WuLC
# @Last Modified time: 2016-07-30 23:08:01
# @Email: liangchaowu5@gmail.com

# Sieve of Eratosthenes
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2: return 0
        primes = [True for i in xrange(n)]
        primes[0] = False
        primes[1] = False
        for i in xrange(2, int(math.sqrt(n))+1):
            if primes[i]:
                for j in xrange(i*i, n, i):
                    primes[j] = False
        return sum(primes)