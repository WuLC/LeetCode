# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2017-10-16 22:55:37
# @Last Modified by:   WuLC
# @Last Modified time: 2017-10-16 23:03:31

# count how many times each number appears and the index where it starts and ends
class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count, index = {}, {}
        max_count = 0
        for i in xrange(len(nums)):
            if nums[i] not in count:
                count[nums[i]] = 1
                index[nums[i]] = [i, i]
            else:
                count[nums[i]] += 1
                index[nums[i]][1] = i
            max_count = max(max_count, count[nums[i]])
        
        min_len = len(nums)
        for k, v in count.items():
            if v == max_count:
                min_len = min(min_len, index[k][1] - index[k][0] + 1)
        return min_len