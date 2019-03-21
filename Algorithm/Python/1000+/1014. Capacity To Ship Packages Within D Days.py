# -*- coding: utf-8 -*-
# Created on Thu Mar 21 2019 21:44:39
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# binary search
class Solution(object):
    def shipWithinDays(self, weights, D):
        """
        :type weights: List[int]
        :type D: int
        :rtype: int
        """
        left, right = 0, 0
        for w in weights:
            left = max(left, w)
            right += w
        
        while left < right:
            mid = left + ((right - left) >> 1)
            tmp, days = 0, 0
            for w in weights:
                if tmp + w > mid:
                    days += 1
                    tmp = 0
                tmp += w
            days += 1
            if days > D:
                left = mid + 1
            else:
                right = mid
        return right