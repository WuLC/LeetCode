# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2017-06-25 15:05:02
# @Last Modified by:   WuLC
# @Last Modified time: 2017-06-25 15:05:42


# O(n) time 
class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_nums, min_nums = nums[:3], nums[:2]
        min_num, max_num = min(max_nums),max(min_nums)
        for k in xrange(2, len(nums)):
            # update max_nums
            if (k >= 3):
                if nums[k] > min_num:
                    for i in xrange(3):
                        if max_nums[i] == min_num:
                            max_nums[i] = nums[k]
                            min_num = min(max_nums)
                            break
            # update min_nums
            if nums[k] < max_num:
                for i in xrange(2):
                    if min_nums[i] == max_num:
                        min_nums[i] = nums[k]
                        max_num = max(min_nums)
                        break
        return max(min_nums[0] * min_nums[1] * max(max_nums), max_nums[0] * max_nums[1] * max_nums[2])
        