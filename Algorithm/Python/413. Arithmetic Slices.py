# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-10-15 17:16:39
# @Last modified by:   WuLC
# @Last Modified time: 2016-10-15 17:22:44
# @Email: liangchaowu5@gmail.com

# Math, O(n) time, O(1) space
# find the array of difference of all consecutive numbers, 
# and go through the difference array to find those continious same number and count the number of arithmetic slices
class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        diff = [A[i+1]-A[i] for i in xrange(len(A)-1)]
        pre, count, result = None, 0, 0
        for i in xrange(len(diff)):
            if pre == None or diff[i] == pre:
                count += 1
            else:
                if count > 1:
                    count -= 1
                    result += (1+count)*count/2
                count = 1
            pre = diff[i]
        if count > 1:
            count -= 1
            result += (1+count)*count/2
        return result