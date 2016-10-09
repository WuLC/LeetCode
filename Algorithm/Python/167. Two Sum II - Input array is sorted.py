# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-08-29 06:46:36
# @Last modified by:   WuLC
# @Last Modified time: 2016-08-29 06:46:52
# @Email: liangchaowu5@gmail.com

# two pointers
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left, right = 0, len(numbers) - 1
        while left < right:
            tmp = numbers[left] + numbers[right]
            if tmp > target:
                right -= 1
            elif tmp < target:
                left += 1
            else:
                return [left+1, right+1]