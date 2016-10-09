# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-06-28 22:19:47
# @Last modified by:   WuLC
# @Last Modified time: 2016-06-28 22:19:57
# @Email: liangchaowu5@gmail.com

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        candidate1, candidate2, count1, count2 = 0, 1, 0, 0
        for i in xrange(len(nums)):
            if nums[i] == candidate1:
                count1 += 1
            elif nums[i] == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1, count1 = nums[i], 1
            elif count2 == 0:
                candidate2, count2 = nums[i], 1
            else:
                count1 -= 1
                count2 -= 1
        if nums.count(candidate1) > len(nums)/3:
            result.append(candidate1)
        if nums.count(candidate2) > len(nums)/3:
            result.append(candidate2)
        return result