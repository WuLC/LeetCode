# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-07-11 09:41:06
# @Last modified by:   WuLC
# @Last Modified time: 2016-07-11 09:41:57
# @Email: liangchaowu5@gmail.com

class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        uglies = [1]
        idx, primes = [0, 0, 0], [2, 3, 5]
        while len(uglies) < n:
            tmp = min(primes[0]*uglies[idx[0]], primes[1]*uglies[idx[1]], primes[2]*uglies[idx[2]])
            if tmp > uglies[-1]:
                uglies.append(tmp)
            for i in xrange(3):
                if primes[i] * uglies[idx[i]] == tmp:
                    idx[i] += 1
        return uglies[-1]