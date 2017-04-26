# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2017-04-26 09:16:02
# @Last modified by:   WuLC
# @Last Modified time: 2017-04-26 09:16:49
# @Email: liangchaowu5@gmail.com


# sort and add up the odd-index numbers
class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        result = 0
        idx = 0
        while idx < len(nums):
            result += nums[idx]
            idx += 2
        return result

