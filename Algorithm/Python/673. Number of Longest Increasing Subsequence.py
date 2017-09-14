# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2017-09-14 23:52:38
# @Last Modified by:   WuLC
# @Last Modified time: 2017-09-14 23:53:46

# dp, time complexity: O(n^2)
# referrer: https://discuss.leetcode.com/topic/103020/java-c-simple-dp-solution-with-explanation
class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        length = [1] * len(nums)
        count = [1] * len(nums)
        length[0], count[0] = 1, 1
        for i in xrange(len(nums)):
            for j in xrange(i):
                if nums[j] < nums[i]:
                    if length[j] + 1 == length[i]:
                        count[i] += count[j]
                    elif length[j] + 1 > length[i]:
                        length[i] = length[j] + 1
                        count[i] = count[j]
        max_len = max(length)
        return sum([count[i] for i in xrange(len(count)) if length[i] == max_len])
                        
        