# -*- coding: utf-8 -*-
# Created on Fri Aug 24 2018 20:58:11
# Author: WuLC
# EMail: liangchaowu5@gmail.com

import heapq
class KthLargest(object):
    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.nums = nums
        heapq.heapify(self.nums)
        while len(self.nums)>k:
            heapq.heappop(self.nums)
            
    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        heapq.heappushpop(self.nums, val)
        return self.nums[0]

    

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)