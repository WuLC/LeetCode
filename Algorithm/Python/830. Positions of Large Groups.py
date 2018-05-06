# -*- coding: utf-8 -*-
# Created on Sun May 06 2018 12:31:30
# Author: WuLC
# EMail: liangchaowu5@gmail.com


# two pointers, O(n) time
class Solution(object):
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        result = []
        left, right = 0, 0
        while right <= len(S):
            if right == len(S) or S[right] != S[right - 1]:
                length = right - left
                if length >= 3:
                    result.append([left, right-1])
                left = right
            right += 1
        return result