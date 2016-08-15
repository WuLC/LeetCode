# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-08-15 14:30:27
# @Last modified by:   WuLC
# @Last Modified time: 2016-08-15 21:47:23
# @Email: liangchaowu5@gmail.com

################################################
# method 1, divide and conquer with memeory
################################################

# use dict as memeory 
class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        non_zero_nums = [1]+[num for num in nums if num>0]+[1]
        return self.helper(0, len(non_zero_nums)-1, non_zero_nums, {})
    
    def helper(self, start, end, nums, cache):
        if start+1==end:
            return 0
        if (start, end) in cache:
            return cache[(start,end)]
        tmp = 0
        for i in xrange(start+1, end):
                left = self.helper(start, i, nums, cache)
                right = self.helper(i, end, nums, cache)
                tmp = max(tmp, left+right+nums[i]*nums[start]*nums[end])
        cache[(start,end)] = tmp
        return tmp


# use list as memory
class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        non_zero_nums = [1]+[num for num in nums if num>0]+[1]
        n = len(non_zero_nums)
        cache = [[0]*n for i in xrange(n)]
        return self.helper(0, n-1, non_zero_nums, cache)
    
    def helper(self, start, end, nums, cache):
        if start+1==end:
            return 0
        if cache[start][end]:
            return cache[start][end]
        tmp = 0
        for i in xrange(start+1, end):
            left = self.helper(start, i, nums, cache)
            right = self.helper(i, end, nums, cache)
            tmp = max(tmp, left+right+nums[i]*nums[start]*nums[end])
        cache[start][end] = tmp
        return tmp       




########################################################            
# method 2, divide and conquer with DP 
########################################################
class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = [1]+[num for num in nums if num>0]+[1]
        n = len(nums)
        dp = [[0]*n for i in xrange(n)]
        for i in xrange(2, n):
            for j in xrange(n-i):
                left, right = j, j+i
                for k in xrange(j+1, j+i):
                    dp[left][right] = max(dp[left][right], nums[left]*nums[k]*nums[right]+dp[left][k]+dp[k][right])
        return dp[0][n-1]