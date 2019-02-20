# -*- coding: utf-8 -*-
# Created on Tue Feb 19 2019 14:19:58
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# greedy, O(n) time
# referer: https://leetcode.com/problems/minimum-number-of-k-consecutive-bit-flips/discuss/239284/C%2B%2B-O(n)-or-O(K)-and-O(n)-or-O(1)
from collections import deque


# O(n) space without modifying the original array
class Solution(object):
    def minKBitFlips(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        result = 0
        queue = deque()
        for i in xrange(len(A)):
            if (A[i] == 0 and (len(queue)&1) == 0) or (A[i] == 1 and (len(queue)&1) == 1):
                result += 1
                queue.append(i+K-1)
            while queue and queue[0] <= i:
                queue.popleft()
        return result if len(queue) == 0 else -1



# O(1) space with modification of the original array
# mark flips with negative values.
class Solution(object):
    def minKBitFlips(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        result, flips = 0, 0
        for i in xrange(len(A)):
            if (A[i] == 0 and (flips&1) == 0) or (A[i] == 1 and (flips&1) == 1):
                result += 1
                flips += 1
                A[i] -= 2
            if i - K + 1 >= 0 and A[i-K+1] < 0:
                flips -= 1
        return result if flips == 0 else -1

