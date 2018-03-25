# -*- coding: utf-8 -*-
# Created on Sun Feb 04 2018 10:18:5
# Author: WuLC
# EMail: liangchaowu5@gmail.com


# dfs
class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        total_sum = sum(nums)
        if total_sum % k != 0 or max(nums) > total_sum/k or total_sum < k or len(nums) < k:
            return False
        self.visited = [0] * len(nums)
        self.target = total_sum/k
        return self.helper(nums, k, 0, 0)
        
    def helper(self, nums, k, curr_sum, idx):
        if k==0:
            return True
        if curr_sum == self.target:
            return self.helper(nums, k-1, 0, 0)
        for i in xrange(idx, len(nums)):
            if self.visited[i]==0:
                self.visited[i] = 1
                if self.helper(nums, k, curr_sum+nums[i], i+1):
                    return True
                self.visited[i] = 0
        return False