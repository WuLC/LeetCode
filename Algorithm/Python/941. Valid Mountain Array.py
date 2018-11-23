# -*- coding: utf-8 -*-
# Created on Fri Nov 23 2018 21:25:42
# Author: WuLC
# EMail: liangchaowu5@gmail.com


# assume two people climbing from left and right, judge whether they finally reach the same peak
class Solution(object):
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        n = len(A)
        left, right = 0, n - 1
        while left + 1 < n and A[left] < A[left + 1]:
            left += 1
        while right - 1 >= 0 and A[right] < A[right - 1]:
            right -= 1
        return left == right and left != 0 and right != n - 1

        