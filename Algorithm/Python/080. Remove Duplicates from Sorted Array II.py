# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-05-19 09:07:22
# @Last modified by:   WuLC
# @Last Modified time: 2016-05-19 09:07:47
# @Email: liangchaowu5@gmail.com

# Two pointers
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        flag, count  = 0, 0
        for i in xrange(1,len(nums)):
            if nums[count] == nums[i] and flag == 0:
                count += 1
                nums[count], nums[i] = nums[i], nums[count]
                flag = 1
            elif nums[count] != nums[i]:
                count += 1
                nums[count], nums[i] = nums[i], nums[count]
                flag = 0
        return count+1
        