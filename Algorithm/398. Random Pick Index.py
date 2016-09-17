# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-09-17 17:15:46
# @Last modified by:   WuLC
# @Last Modified time: 2016-09-17 17:16:34
# @Email: liangchaowu5@gmail.com


# reservoir sampling, O(1) space, O(n) time
class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        :type numsSize: int
        """
        self.nums = nums

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        idx, count = None, 0
        for i in xrange(len(self.nums)):
            if self.nums[i] == target:
                if random.randint(0, count) == 0:
                    idx = i
                count += 1
        return idx
            