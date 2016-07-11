# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-07-11 13:51:55
# @Last modified by:   WuLC
# @Last Modified time: 2016-07-11 13:52:09
# @Email: liangchaowu5@gmail.com

class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        uglies = [1]
        idx = [0 for i in xrange(len(primes))]
        while len(uglies) < n:
            tmp = None
            for i in xrange(len(primes)):
                tmp = uglies[idx[i]] * primes[i] if tmp == None else min(tmp, uglies[idx[i]] * primes[i])
            if tmp > uglies[-1]:
                uglies.append(tmp)
            for j in xrange(len(idx)):
                if uglies[idx[j]] * primes[j] == tmp:
                    idx[j] += 1 
        return uglies[-1]