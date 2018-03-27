# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-06-07 15:24:56
# @Last modified by:   WuLC
# @Last Modified time: 2016-06-07 15:25:08
# @Email: liangchaowu5@gmail.com

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return self.helper(nums, 0, len(nums)-1, k)
        
    def helper(self, nums, left, right, k):
        if left > right:
            return 
        i, j = left, right
        while i < j:
            while i<j and nums[j] >= nums[left]:
                j -= 1
            while i<j and nums[i] <= nums[left]:
                i += 1
            if i < j:
                nums[i], nums[j] = nums[j], nums[i]
        nums[i], nums[left] = nums[left], nums[i]
        if i == len(nums)-k:
            return nums[i]
        elif i< len(nums)-k:
            return self.helper(nums, i+1, right, k)
        else:
            return self.helper(nums, left, i-1, k) 
        
# solution 2, use heap to keep the k largest numbers
import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heap = []
        for num in nums:
            if len(heap) < k:
                heapq.heappush(heap, num)
            else:
                heapq.heappushpop(heap, num)
        return heap[0]