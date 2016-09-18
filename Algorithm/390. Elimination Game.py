# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2016-09-18 00:22:48
# @Last modified by:   WuLC
# @Last Modified time: 2016-09-18 23:45:39
# @Email: liangchaowu5@gmail.com

# MLE
class Solution(object):
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        nums = [i for i in xrange(1, n+1)]
        left_to_right = True
        while len(nums) > 1:
            if left_to_right:
                nums = nums[1::2]
                left_to_right = False
            else:
                nums = nums[-2::-2][::-1]
                left_to_right = True
        return nums[0]


# maintain the head of each subsequence till there is only one element in the subsquence
# notice that the difference of neighbor elements of each subquence is 2^m, in which m is the number of operation of elimination 
class Solution(object):
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        head, step, remain = 1, 1, n
        left = True
        while remain > 1:
            if left or remain % 2 == 1:
                head += step
            step *= 2
            remain /= 2
            left = not left
        return head