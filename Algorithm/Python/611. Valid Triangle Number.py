# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2017-06-11 13:02:45
# @Last modified by:   LC
# @Last Modified time: 2017-06-11 13:20:10
# @Email: liangchaowu5@gmail.com


# dfs, TLE
class Solution(object):
    
    def __init__(self):
        self.result = 0
        
        
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.result = 0
        nums.sort()
        self.dfs(nums, 0, [])
        return self.result
        
        
    def dfs(self, nums, idx, tmp):
        for i in xrange(idx, len(nums)):
            if len(tmp) < 2:
                self.dfs(nums, i+1, tmp+[nums[i]])
            else:
                if sum(tmp) > nums[i]:
                    self.result += 1
                else:
                    return

# three pointers, AC
class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        result = 0
        for i in xrange(2, len(nums)):
            left, right = 0, i-1
            while left < right:
                if nums[left] + nums[right] > nums[i]:
                    result += (right - left)
                    right -= 1
                else:
                    left += 1
        return result