# -*- coding: utf-8 -*-
# Created on Sun Jul 22 2018 10:53:39
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# binary search
class Solution(object):
    def minEatingSpeed(self, piles, H):
        """
        :type piles: List[int]
        :type H: int
        :rtype: int
        """
        left, right = max(1, sum(piles)//H), max(piles)  # sum(piles)//H may be 0
        while left < right:
            mid = left + ((right - left)>>1)
            tmp = sum(math.ceil(pile*1.0/mid) for pile in piles)
            if tmp > H:
                left = mid + 1
            else:
                right = mid
        return right