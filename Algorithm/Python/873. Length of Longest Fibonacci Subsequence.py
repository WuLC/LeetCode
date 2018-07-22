# -*- coding: utf-8 -*-
# Created on Sun Jul 22 2018 20:22:31
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# use any two numbers as starting numbers and construct the sequence
class Solution(object):
    def lenLongestFibSubseq(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        nums = set(A)
        result = 0
        for i in xrange(len(A)):         
            for j in xrange(i+1, len(A)):
                tmp = 2   
                a, b = A[i], A[j]
                while a+b in nums:
                    a, b = b, a+b
                    tmp += 1
                result = max(result, tmp)
        return result if result > 2 else 0