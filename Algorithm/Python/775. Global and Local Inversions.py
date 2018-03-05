# -*- coding: utf-8 -*-
# Created on Sun Jan 28 2018 13:48:4
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# global inversions is equal to the number of local inversions
# only when any two neighbor numbers in list [0,1,2,....N-1] change with each other and just once
class Solution(object):
    def isIdealPermutation(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        for i in xrange(len(A)-1):
            if A[i] > A [i+1]:
                if A[i] != i+1 or A[i+1] != i:
                    return False
        return True
        