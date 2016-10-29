# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-10-28 23:22:38
# @Last modified by:   WuLC
# @Last Modified time: 2016-10-30 00:09:16
# @Email: liangchaowu5@gmail.com

# referer: https://discuss.leetcode.com/topic/50489/c-clean-and-short-solution/2

# bases: (a*b)%c = (a%c)*(b%c)%c
# maximal recursion exceed
class Solution(object):
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        if len(b) == 1:
            return pow(a, b[0]) % 1337
        else:
            d = b.pop()
            return self.superPow(self.superPow(a, b), [1,0]) * self.superPow(a, [d]) % 1337


# same idea but different implementation
class Solution(object):
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        def pow_mod(a, k): 
            """return the value of pow(a,k)%1337, pay attention to the method to avoid overflow"""
            a = a % 1337
            result = 1
            for i in xrange(k):
                result = (result*a)%1337
            return result
        if len(b) == 1:
            return pow_mod(a, b[0])
        else:
            d = b.pop()
            return pow_mod(self.superPow(a, b), 10) * pow_mod(a, d) % 1337