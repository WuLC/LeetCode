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
        total = sum(nums)
        if total % k != 0 or total < k or len(nums) < k:
            return False
        self.target = total/k
        self.nums = sorted(nums, reverse = True)
        if self.nums[0] > self.target:
            return False
        self.visited = [0] * len(nums)
        return self.dfs(k, 0, 0)
    
    
    def dfs(self, k, idx, tmp):
        if k==1:
            return True
        elif tmp == self.target:
            return self.dfs(k-1, 0, 0)
        else:
            for i in xrange(idx, len(self.nums)):
                if self.visited[i] == 0 and tmp + self.nums[i] <= self.target:
                    self.visited[i] = 1
                    if self.dfs(k, idx+1, tmp + self.nums[i]):
                        return True
                    self.visited[i] = 0
        return False