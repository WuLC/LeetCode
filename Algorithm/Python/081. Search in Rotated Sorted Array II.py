# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-05-19 10:17:15
# @Last modified by:   WuLC
# @Last Modified time: 2016-05-19 10:18:13
# @Email: liangchaowu5@gmail.com

# binary search in recurse mode 
# deal with case like: [1,1,1,1,1,2,3,1,1]
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if len(nums) == 0:
            return False
        n = len(nums)
        if self.helper(nums, 0, n-1,target):
            return True
        else:
            return False
            
            
    def helper(self,nums,left,right,target):
        if left > right:
            return False
        if left == right:
            return nums[left] == target
        else:
            mid = (left+right)/2
            if nums[mid] == target:
                return True
            elif  nums[left]<=target<nums[mid]:
                return self.helper(nums,left,mid-1,target)
            elif nums[mid]<target<=nums[right]:
                return self.helper(nums,mid+1,right,target)
            else:
                return self.helper(nums,mid+1,right,target) or self.helper(nums,left,mid-1,target)
        
        