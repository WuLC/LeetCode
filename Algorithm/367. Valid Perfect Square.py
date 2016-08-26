# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-08-26 21:28:19
# @Last modified by:   WuLC
# @Last Modified time: 2016-08-26 21:28:26
# @Email: liangchaowu5@gmail.com

class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        left, right = 1, num
        while left < right:
            mid = left + (right - left)/2
            area = mid*mid
            if area == num:
                return True
            elif area > num:
                right = mid -1
            else:
                left = mid + 1
        if left*left == num:
            return True
        return False