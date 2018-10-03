# -*- coding: utf-8 -*-
# Created on Wed Oct 03 2018 12:36:0
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# O(n) time, compare the left_max number with current number
class Solution(object):
    def partitionDisjoint(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        left_max, curr_max, idx = A[0], A[0], 0
        for i in xrange(1, len(A)):
            if left_max>A[i]:
                left_max = curr_max
                idx = i
            else:
                curr_max = max(curr_max, A[i])
        return idx+1