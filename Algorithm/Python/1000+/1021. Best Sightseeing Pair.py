# -*- coding: utf-8 -*-
# Created on Fri Mar 29 2019 20:37:15
# Author: WuLC
# EMail: liangchaowu5@gmail.com


# two pass solution, O(n) time, O(n) space
from collections import deque

class Solution(object):
    def maxScoreSightseeingPair(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        right2left_max, curr = deque(), -50000
        for i in xrange(len(A)-1, -1, -1):
            curr = max(curr, A[i] - i)
            right2left_max.appendleft(curr)

        result, left_max = 0, 0
        for i in xrange(len(A) - 1):
            left_max = max(left_max, A[i] + i)
            result = max(result, left_max + right2left_max[i+1])
        return result

# one pass solution, O(n) time, O(1) space
# iterate from left to right, make curr the maximum of A[i]+i-j
class Solution(object):
    def maxScoreSightseeingPair(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        result, curr = 0, A[0] - 1
        for i in xrange(1, len(A)):
            result = max(result, curr + A[i])
            curr = max(curr - 1, A[i] - 1)
        return result