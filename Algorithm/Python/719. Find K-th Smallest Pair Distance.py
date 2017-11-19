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

