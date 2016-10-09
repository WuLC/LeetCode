# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2016-04-08 15:02:26
# @Last modified by:   LC
# @Last Modified time: 2016-04-10 16:22:30
# @Email: liangchaowu5@gmail.com



# 找到与target相同的数，从这个位置往左右递归找
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) == 0:
            return [-1,-1]
        
        posi = [-1,-1]
        left = 0
        right = len(nums)-1
        self.find(nums,target,left,right,posi)
        return posi
                
    def find(self,nums,target,left,right,position):
        while left < right:
            mid = (left + right)/2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid]> target:
                right = mid - 1
            else:
                if position[0] == -1 or position[0]>mid:
                    position[0] = mid
                if position[1] == -1 or position[1]<mid:
                    position[1] = mid
                self.find(nums,target,left,mid-1,position)
                self.find(nums,target,mid+1,right,position)
                return           # 这里需要有返回，否则程序回到上一次找到这个值的地方会一直死循环递归下去
        if nums[left]==target:
            if position[0] == -1 or position[0]>left:
                position[0] = left
            if position[1] == -1 or position[1]<right:
                position[1] = right
            
                
            
        