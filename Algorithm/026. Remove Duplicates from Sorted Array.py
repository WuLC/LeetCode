# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2016-03-31 09:54:41
# @Last modified by:   LC
# @Last Modified time: 2016-04-10 16:23:14
# @Email: liangchaowu5@gmail.com


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return len(nums)
        
        count = 0
        for i in range(1,len(nums)):
            if not nums[i] == nums[count]:
                count+=1
                nums[count]=nums[i]
        return count+1
        