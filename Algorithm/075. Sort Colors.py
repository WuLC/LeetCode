# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-05-14 16:34:30
# @Last modified by:   WuLC
# @Last Modified time: 2016-05-14 19:46:14
# @Email: liangchaowu5@gmail.com

# method1 ,count the number of 0,1,2 in the list
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        tmp = {0:0,1:0,2:0}
        for i in xrange(n):
            tmp[nums[i]] += 1
        cur = 0
        for j in xrange(3):
            for k in xrange(tmp[j]):
                nums[cur] = j
                cur += 1
            
        
# method2, two pointers            
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        left, right = 0, n-1
        while left<right:
             while right > left and nums[right]==2:
                 right -= 1
             while right > left and nums[left] != 2:
                 left += 1
             if left >= right:
                 break
             nums[left],nums[right] = nums[right],nums[left]
             left += 1
             right -=1 
        if left == right and nums[left] == 2:
            right -= 1
            
        left = 0
        while left< right:
             while right > left and nums[right]==1:
                 right -= 1
             while right > left and nums[left] != 1:
                 left += 1
             if left >= right:
                 break
             nums[left],nums[right] = nums[right],nums[left]
             left += 1
             right -=1             
            
        
        
                 
            