#
# @lc app=leetcode id=376 lang=python
#
# [376] Wiggle Subsequence
#

# @lc code=start


# dp with O(n^2) time complexity
class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n, result = len(nums), 0
        dp = [[1] * n for _ in range(2)]
        for i in range(n):
            if i > 0:
                for j in range(i):
                    if nums[j] > nums[i]:
                        dp[0][i] = max(dp[1][j]+1, dp[0][i])
                    elif nums[j] < nums[i]:
                        dp[1][i] = max(dp[0][j]+1, dp[1][i])
            result = max(result, max(dp[0][i], dp[1][i]))
        return result

        
# @lc code=end

