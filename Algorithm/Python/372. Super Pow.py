# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-10-28 23:22:38
# @Last modified by:   WuLC
# @Last Modified time: 2016-10-28 23:47:18
# @Email: liangchaowu5@gmail.com

# referer: https://discuss.leetcode.com/topic/50489/c-clean-and-short-solution/2

# maxmum recursion exceed
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
            return (self.superPow(self.superPow(a, b), [1,0]) * self.superPow(a, [d])) % 1337


# same idea as the above
class Solution(object):
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        def pow_mod(a, k): # k<10
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