# -*- coding: utf-8 -*-
# Created on Sun Mar 03 2019 10:55:59
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# two pointers, O(n) time, O(1) space
class Solution(object):
    def longestOnes(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        result = 0
        left, right = 0, 0
        while right < len(A):
            if A[right] == 0:
                K -= 1
            while K < 0:
                if A[left] == 0:
                    K += 1
                left += 1
            result = max(right - left + 1, result)
            right += 1
        return result

# another solution recording the index of 0 so that left can move multiple steps at a time
class Solution(object):
    def longestOnes(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        result = 0
        left, right = 0, 0
        zeros = collections.deque()
        while right < len(A):
            if A[right] == 0:
                zeros.append(right)
                K -= 1
            while K < 0:
                left = zeros[0]+1
                zeros.popleft()
                K += 1
            result = max(right - left + 1, result)
            right += 1
        return result