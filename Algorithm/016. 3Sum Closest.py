# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2016-03-10 17:38:42
# @Last modified by:   LC
# @Last Modified time: 2016-04-10 16:24:30
# @Email: liangchaowu5@gmail.com

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        
        nums.sort()
        min = 1000000
        
        for i in range(len(nums)-2):
            j = i+1
            k = len(nums)-1
            while j<k:
                sum = nums[i]+nums[j]+nums[k]
                if sum > target:
                    gap = abs(sum -target)
                    if min>gap:
                        min = gap
                        result = sum
                    k-=1
                elif sum < target:
                    gap = abs(target - sum)
                    if min > gap:
                        min = gap
                        result = sum
                    j+=1
                else:
                    result = sum
                    return result
        return result
                
                    
                    
