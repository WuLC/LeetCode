#
# @lc app=leetcode id=718 lang=python
#
# [718] Maximum Length of Repeated Subarray
#

# @lc code=start

class Solution(object):
    def findLength(self, nums1, nums2):
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
                if nums1[i] == nums2[j]:
                    dp[i+1][j+1] = dp[i][j] + 1
                result = max(dp[i+1][j+1], result)
        return result

        
# @lc code=end

