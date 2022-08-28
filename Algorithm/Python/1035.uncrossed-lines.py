#
# @lc app=leetcode id=1035 lang=python
#
# [1035] Uncrossed Lines
#

# @lc code=start
class Solution(object):
    def maxUncrossedLines(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        m, n = len(nums1), len(nums2)
        result = 0 
        dp = [[0]*(n+1) for _ in range(m+1)]
        for i in range(m):
            for j in range(n):
                dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])
                if nums1[i] == nums2[j]:
                    dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j]+1)
                result = max(result, dp[i+1][j+1])
        return result

        
        
# @lc code=end

