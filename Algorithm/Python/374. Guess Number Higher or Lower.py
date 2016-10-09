# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2016-08-26 21:18:31
# @Last modified by:   WuLC
# @Last Modified time: 2016-08-26 21:18:50
# @Email: liangchaowu5@gmail.com

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 1, n
        while left<right:
            mid = (left+right)/2
            tmp = guess(mid)
            if tmp==0:
                return mid
            elif tmp == 1:
                left = mid+1
            else:
                right = mid-1
        return left
        