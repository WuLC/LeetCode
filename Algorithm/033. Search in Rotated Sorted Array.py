# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2016-04-07 09:47:36
# @Last modified by:   LC
# @Last Modified time: 2016-04-10 16:22:37
# @Email: liangchaowu5@gmail.com


# 方法一，先找到最小list中最小值的下标，下标会将原来的list分为两个sorted list
# 判断target在哪个sorted list然后对这个sorted list进行二分查找即可
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return -1
        left = 0 
        right = len(nums)-1
        while left<right:
            mid = (left+ right)/2
            if nums[mid]>nums[right]:
                left = mid + 1
            else:
                right = mid
        minIndex = left
        
        if minIndex == 0:
            if nums[minIndex]<=target<= nums[len(nums)-1]:
                return self.binarySearch(minIndex,len(nums)-1,nums,target)
            else:
                return -1
        else:
            if nums[0]<= target<=nums[minIndex-1]:
                return self.binarySearch(0,minIndex-1,nums,target)
            elif nums[minIndex]<= target<=nums[len(nums)-1]:
                return self.binarySearch(minIndex,len(nums)-1,nums,target)
            else:
                return -1

    # 对一个sorted list的经典二分查找
    def binarySearch(self,left,right,nums,target):
        while left < right:
            mid = (left + right)/2
            if nums[mid] == target:
                return mid
            elif nums[mid]>target:
                right = mid -1
            else:
                left = mid+1
        if nums[left] == target:
            return left
        else:
            return -1


## 方法二:只需遍历一次，每次可以去掉一半的元素
## 参考：https://leetcode.com/discuss/41134/java-ac-solution-using-once-binary-search
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return -1
        left = 0 
        right = len(nums) - 1
        
        while left < right:
            mid = (left + right)/2
            if nums[mid] == target:
                return mid
                
            if nums[left] <= nums[mid]:
                if nums[left]<=target<=nums[mid]:
                    right = mid - 1   # mid要减去1，否则两个元素的时候会导致死循环
                else:
                    left = mid+1
            
            if nums[mid] <= nums[right]:
                if nums[mid]<=target<=nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        
        if nums[left] == target:
            return left
        else:
            return -1
                
