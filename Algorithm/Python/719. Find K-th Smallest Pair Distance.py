# -*- coding: utf-8 -*-
# Created on Sun Nov 19 2017 17:5:38
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# naive heapq, TLE
import heapq
class Solution(object):
    def smallestDistancePair(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums = sorted(nums)
        distances = []
        for i in xrange(len(nums)-1):
            tmp = []
            for j in xrange(i+1, len(nums)):
                tmp.append(nums[j] - nums[i])
            distances.append(tmp)
        heap = heapq.merge(*distances)
        count = k
        for num in heap:
            if count == 1:
                return num
            count -= 1 


# binary search, still TLE
class Solution(object):
    def smallestDistancePair(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        min_dist, max_dist = nums[-1] - nums[0], nums[-1] - nums[0]
        for i in xrange(1, len(nums)):
            min_dist = min(min_dist, nums[i] - nums[i-1])
        left, right = min_dist, max_dist
        while left < right:
            mid = left + ((right-left)>>1);
            if self.countPairs(nums, mid) < k:
                left = mid + 1
            else:
                right = mid
        return left 
    
    def countPairs(self, nums, dist):
        """number of pairs whose distance is no more than dist"""
        count = 0
        for i in xrange(len(nums)):
            j = i + 1
            while j < len(nums) and nums[j] - nums[i] <= dist:
                count += 1
                j += 1
        return count
        