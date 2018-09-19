# -*- coding: utf-8 -*-
# Created on Wed Sep 19 2018 15:33:59
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# two pointers
class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        result = [0]*len(A)
        left, right = 0, len(A)-1
        for num in A:
            if num&1:
                result[right] = num
                right -= 1
            else:
                result[left] = num
                left += 1
        return result