#
# @lc app=leetcode id=416 lang=python
#
# [416] Partition Equal Subset Sum
#

# @lc code=start
class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums_sum = sum(nums)
        if len(nums) <= 1 or (nums_sum%2) > 0:
            return False
        m, n = len(nums), nums_sum>>1
        dp = [[False]*(n+1) for _ in range(m+1)]

        for i in range(1, m+1):
            for j in range(n+1):
                if j == 0:
                    dp[i][j] = True
                    continue
                if nums[i-1] > (nums_sum>>1):
                    return False
                if nums[i-1] == (nums_sum>>1):
                    return True            
                dp[i][j] = dp[i-1][j] or (j >= nums[i-1] and dp[i-1][j-nums[i-1]])
            if dp[i][n]:
                return True
        return False
        
# @lc code=end

