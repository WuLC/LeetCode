# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-08-22 14:11:51
# @Last modified by:   WuLC
# @Last Modified time: 2016-08-22 23:03:35
# @Email: liangchaowu5@gmail.com

# method 1
# backtrack to find all combinations with elements from smaller to higher(the same as 39.combination sum)
# then do premutation of of these combination with duplicate elements 
class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        result = [0]
        nums.sort()
        self.helper(0, nums, [], target, result)
        return result[0]
        
    def helper(self, idx, nums, path, target, result):
        if target == 0:
            result[0] += self.permutation(0, path)
            return
        for i in xrange(idx, len(nums)):
            if target - nums[i] < 0:
                return
            self.helper(i, nums, path+[nums[i]], target - nums[i], result)
    
    #  permutation of duplicate elements
    def permutation(self,idx, nums):
        if idx == len(nums) - 1:
            return 1
        count = 0
        for i in xrange(idx, len(nums)):
            if nums[i] in nums[idx:i]:
                continue
            else:
                nums[idx], nums[i] = nums[i], nums[idx]
                count += self.permutation(idx+1, nums)
                nums[idx], nums[i] = nums[i], nums[idx]
        return count




# method 2, recursive method，TLE
class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target == 0:
            return 1
        result = 0
        for num in nums:
            if target >= num:
                result += self.combinationSum4(nums, target - num)
        return result
            


# method 3,based on method 2, add DP, AC
class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        cache = {}
        cache[0] = 1
        return self.helper(nums, target, cache)
    
    
    def helper(self, nums, target, cache):
        if target in cache:
            return cache[target]
        count = 0
        for num in nums:
            if target >= num:
                count += self.helper(nums, target-num, cache)
        cache[target] =  count
        return count


# method 4, DP from bottom to top，while DP in the method 3 is from top to bottom, AC
class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        dp = [0 for i in xrange(target+1)]
        dp[0] = 1
        for i in xrange(1, target+1):
            for num in nums:
                if i>= num:
                    dp[i] += dp[i-num]
        return dp[target]
        