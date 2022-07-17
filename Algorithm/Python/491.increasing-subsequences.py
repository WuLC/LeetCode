#
# @lc app=leetcode id=491 lang=python
#
# [491] Increasing Subsequences
#

# @lc code=start
class Solution(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result, candidate = [], []


        def dfs(idx):
            if len(candidate) >= 2:
                result.append(candidate[:])
            used = set()
            for i in range(idx, len(nums)):
                if nums[i] in used:
                    continue
                if len(candidate) == 0 or nums[i] >= candidate[-1]:
                    candidate.append(nums[i])
                    used.add(nums[i])
                    dfs(i+1)
                    candidate.pop()
        dfs(0) 
        return result 
        
# @lc code=end

