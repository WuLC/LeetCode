# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2017-09-12 13:12:56
# @Last Modified by:   WuLC
# @Last Modified time: 2017-09-12 13:13:45


# priority queue, similar to merge k sorted list
# each time the heap contains one element of each list
import heapq
class Solution(object):
    def smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        pq = []
        max_val = -10 ** 5
        for i in xrange(len(nums)):
            heapq.heappush(pq,(nums[i][0], i, 0))
            max_val = max(max_val, nums[i][0])
        smallest_range = 2 * 10**5    
        result = None
        while len(pq) == len(nums):
            val, i, idx = heapq.heappop(pq)
            if smallest_range > max_val - val:
                result = [val, max_val]
                smallest_range = max_val - val
            if idx + 1 < len(nums[i]):
                heapq.heappush(pq, (nums[i][idx+1], i, idx + 1))
                max_val = max(max_val, nums[i][idx+1])
        return result
        
