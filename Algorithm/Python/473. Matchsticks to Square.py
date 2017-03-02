# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2017-03-03 00:02:54
# @Last modified by:   WuLC
# @Last Modified time: 2017-03-03 00:03:12
# @Email: liangchaowu5@gmail.com


# dfs
class Solution(object):
    def makesquare(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums_sum = sum(nums)
        if nums_sum == 0 or nums_sum % 4  != 0: return False
        length = (nums_sum >> 2)
        nums.sort(reverse = True)
        sums= [length for _ in xrange(4)]
        return self.helper(sums, 0, nums)
    
    def helper(self, sums, idx, nums):
        if idx == len(nums):
            return True
        
        for i in xrange(4):
            if sums[i] >= nums[idx]:
                sums[i] -= nums[idx]
                if self.helper(sums, idx+1, nums):
                    return True
                sums[i] += nums[idx]
        return False