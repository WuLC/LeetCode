#
# @lc app=leetcode id=377 lang=python
#
# [377] Combination Sum IV
#

# @lc code=start

class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        dp = [0] * (target + 1)
        dp[0] = 1
        for num in nums:
            for i in range(target+1):
        # for i in range(1, target+1):
        #     for num in nums:
                if i >= num:
                    dp[i] += dp[i-num]
        return dp[target]

# backtrack will TLE
# class Solution(object):
#     def combinationSum4(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: int
#         """
#         self.result = 0
#         self.dfs(0, 0, nums, target)
#         return self.result

#     def dfs(self, idx, curr_sum, nums, target):
#         if curr_sum >= target:
#             if curr_sum == target:
#                 self.result += 1
#             return
#         for i in range(idx, len(nums)):
#             self.dfs(idx, curr_sum+nums[i], nums, target)
    
# @lc code=end

