#
# @lc app=leetcode id=78 lang=python
#
# [78] Subsets
#

# @lc code=start
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result, candidate = [], []

        def dfs(idx):
            result.append(candidate[:])
            if idx == len(nums):
                return
            for i in range(idx, len(nums)):
                candidate.append(nums[i])
                dfs(i+1)
                candidate.pop()

        dfs(0)
        return result
    
# @lc code=end

