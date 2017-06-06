# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2017-06-06 20:54:33
# @Last modified by:   WuLC
# @Last Modified time: 2017-06-06 21:03:23
# @Email: liangchaowu5@gmail.com


# O(n) time, check each plot by checking its two neighbor
class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        count = 0
        flowerbed = [0] + flowerbed + [0]
        for i in xrange(1, len(flowerbed) - 1):
            if flowerbed[i] == 0 and flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                count += 1
                flowerbed[i] = 1
        return True if count >= n else False