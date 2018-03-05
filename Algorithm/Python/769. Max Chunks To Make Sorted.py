# -*- coding: utf-8 -*-
# Created on Mon Jan 29 2018 21:46:44
# Author: WuLC
# EMail: liangchaowu5@gmail.com


# two pointers
class Solution(object):
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        left_idx, curr_idx = len(arr) - 1, len(arr) - 1
        count = 0
        while curr_idx >= 0:
            left_idx = min(left_idx, arr[curr_idx])
            if left_idx == curr_idx:
                count += 1
            curr_idx -= 1
        return count