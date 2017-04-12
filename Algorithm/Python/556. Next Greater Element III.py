# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2017-04-12 10:45:55
# @Last modified by:   LC
# @Last Modified time: 2017-04-12 10:51:31
# @Email: liangchaowu5@gmail.com

# O(n^2) time complexity
# traverse from end to start, exchange it with the smallest digit after it that is greater than it 
# then concate the two parts and return the result
class Solution(object):
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        s = list(str(n))
        for i in reversed(xrange(len(s))):
            max_idx = None
            for j in xrange(i+1, len(s)):
                if s[j] > s[i]:
                    if max_idx == None or s[max_idx] > s[j]:
                        max_idx = j
            if max_idx:
                s[i], s[max_idx] = s[max_idx], s[i]
                next_greater = int(''.join(s[:i+1]+sorted(s[i+1:])))
                # next greater element need to be in the range of integer
                return next_greater if next_greater < (1<<31) else -1 
        return -1