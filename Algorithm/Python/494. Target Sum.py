# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2017-02-02 21:34:27
# @Last modified by:   WuLC
# @Last Modified time: 2017-02-05 01:41:24
# @Email: liangchaowu5@gmail.com


# naive dfs, O(2^n), TLE
class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        self.result = 0
        self.dfs(0, 0, S, nums)
        return self.result
        
    def dfs(self, idx, count, S, nums):
        if idx == len(nums):
            if count == S:
                self.result += 1
            return
        else:
            for flag in [1,-1]:
                self.dfs(idx+1, count+flag*nums[idx], S, nums)


# naive recursive, TLE
class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        if len(nums) == 0:
            return 1 if S == 0 else 0
        curr_num = nums.pop()
        return self.findTargetSumWays(nums[:], S - curr_num) + self.findTargetSumWays(nums[:], S + curr_num)
        

# dp, AC
class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        count = collections.defaultdict(int)
        count[0] = 1
        for num in nums:
            tmp = collections.defaultdict(int)
            for k,v in count.items():
                tmp[k + num] += v
                tmp[k - num] += v
            count = tmp
        return count[S]