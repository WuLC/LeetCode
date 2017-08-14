# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2017-08-14 17:32:24
# @Last Modified by:   WuLC
# @Last Modified time: 2017-08-14 17:34:17


# recursive with cache
# math: if n in prime, the min steps is n, else judge if n is odd or even and recursivly count the min steps
class Solution(object):
    
    def __init__(self):
        self.cache = {}
        self.cache[1] = 0
        
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.helper(n)
    
    def helper(self, n):
        if n not in self.cache:
            count = n
            if not self.isPrime(n):
                if (n & 1) == 0: # even number
                    count = 2 + self.helper(n>>1)
                else:
                    for i in xrange(2, int(math.sqrt(n)+1)):
                        if n % i == 0:
                            count = min([count, i + self.helper(n/i), n/i + self.helper(i)])
            self.cache[n] = count
        return self.cache[n]
    
    def isPrime(self, n):
        for i in xrange(2, int(math.sqrt(n)+1)):
            if n % i == 0:
                return False
        return True
