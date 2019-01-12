# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-06-11 13:19:29
# @Last modified by:   WuLC
# @Last Modified time: 2016-06-11 13:19:45
# @Email: liangchaowu5@gmail.com


# DP
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.insert(0, 0)
        for i in xrange(3, len(nums)):
            nums[i] = max(nums[i]+nums[i-2], nums[i]+nums[i-3])
        return max(nums)

# dp in another way, when at certain index, robber may not rob this index
# constant space
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        p1, p2, p3 = 0, 0, 0
        for num in nums:
            tmp = max(p3, p2 + num)
            p1, p2 = p2, p3
            p3 = tmp
        return p3