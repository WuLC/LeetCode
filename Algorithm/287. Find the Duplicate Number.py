# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-07-17 15:26:40
# @Last modified by:   WuLC
# @Last Modified time: 2016-07-18 08:24:53
# @Email: liangchaowu5@gmail.com

# quick sort, O(1) space, O(nlogn) time complexity, but need to modify the array
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.helper(nums, 0, len(nums)-1)

    def helper(self, nums, left, right):
        if left >= right:
            return
        pivot, end = left, right
        while left < right:
            while left < right and nums[pivot] <= nums[right]:
                if nums[pivot] == nums[right] and pivot != right:
                    return nums[pivot]
                right -= 1
            while left < right and nums[pivot] >= nums[left]:
                if nums[pivot] == nums[left] and pivot != left:
                    return nums[pivot]
                left += 1
            if left < right:
                nums[left], nums[right] = nums[right], nums[left]
        if nums[left] == nums[pivot] and left != pivot:
            return nums[pivot]
            
        nums[pivot], nums[left] = nums[left], nums[pivot]
        r1 = self.helper(nums, pivot, left-1)
        if r1: 
            return r1
        r2 = self.helper(nums, left+1, end)
        if r2:
            return r2


# method 2, two pointers , one move two steps at a time, the other move one step at a time
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow = nums[0]
        fast = nums[nums[0]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        fast = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow
                