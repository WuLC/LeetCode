#
# @lc app=leetcode id=213 lang=python
#
# [213] House Robber II
#

# @lc code=start
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def helper(start, end):
            dp = [0] * (end - start + 2)
            for i in range(start, end+1):
                if i == start:
                    dp[i-start+1] = nums[i]
                else:
                    dp[i-start+1] = max(dp[i-start], dp[i-start-1] + nums[i])
            return dp[-1]
        
        return max(helper(0, len(nums) - 2), helper(1, len(nums) -1)) if len(nums) > 1 else sum(nums)

        
# @lc code=end

