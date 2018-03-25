# -*- coding: utf-8 -*-
# Created on Sun Mar 25 2018 20:32:48
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# dfs
# change it to find certain number of elements with fixed sum
# 1.0 == 1 return True in python
class Solution(object):
    def splitArraySameAverage(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        average = sum(A)*1.0/len(A)
        for i in xrange(1, len(A)/2+1):
            if int(average*i) == average*i: # ensure the sum must be integer
                if self.helper(i, average*i, 0, A):
                    return True
        return False
                
    
    def helper(self, count, curr_sum, idx, A):
        if count == 0 and curr_sum == 0:
            return True
        elif count == 0 or curr_sum == 0:
            return False
        for i in xrange(idx, len(A)):
            if A[i] <= curr_sum and self.helper(count-1, curr_sum-A[i], i+1, A):
                return True
        return False