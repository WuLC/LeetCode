# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2017-08-28 19:03:24
# @Last Modified by:   LC
# @Last Modified time: 2017-08-28 19:06:53

# greedy
# when nums[i] < nums[i-1]
# decrease nums[i-1] or increase nums[i]
# increase nums[i] only when nums[i-2] > nums[i]
# else decrease nums[i-1]
class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        count = 0
        for i in xrange(1, len(nums)):
            if nums[i-1] > nums[i]:
                count += 1
                if i - 2 >= 0 and nums[i - 2] > nums[i]:
                    nums[i] = nums[i-1]
                else:
                    nums[i-1] = nums[i]
                if count > 1:
                    return False
        return True