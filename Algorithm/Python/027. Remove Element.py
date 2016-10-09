# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2016-03-31 10:11:49
# @Last modified by:   LC
# @Last Modified time: 2016-04-10 16:23:11
# @Email: liangchaowu5@gmail.com


class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        
        l = 0
        r = len(nums)-1
        while l<r:
            if nums[r] == val:
                r-=1
                continue
            
            if nums[l] == val:
                nums[l],nums[r] = nums[r],nums[l]
                l += 1
                r -= 1
            else:
                l += 1
        
        if l == r: # 有可能l>r
            if not nums[l] == val:
                l+=1
        return l
            
                
        