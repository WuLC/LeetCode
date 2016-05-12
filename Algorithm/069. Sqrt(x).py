# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-05-12 16:08:55
# @Last modified by:   WuLC
# @Last Modified time: 2016-05-12 16:17:56
# @Email: liangchaowu5@gmail.com

# when the result is not integer, get the interger part of the result
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        left = 0
        right = x
        while left < right:
            mid = (left+right)/2
            tmp = mid*mid
            if mid*mid == x:
                return mid
            elif tmp > x:
                right = mid - 1
            elif tmp < x:
                left = mid + 1
        if left*left > x:
            return left - 1
        else:
            return left