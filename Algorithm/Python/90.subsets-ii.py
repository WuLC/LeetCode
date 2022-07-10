#
# @lc app=leetcode id=90 lang=python
#
# [90] Subsets II
#

# @lc code=start
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result, candidate = [], []
        used = [False] * len(nums)

        def dfs(idx):
            result.append(candidate[:])
            for i in range(idx, len(nums)):
                # remove duplicate
                if i > 0 and nums[i] == nums[i-1] and (not used[i-1]):
                    continue
                candidate.append(nums[i])
                used[i] = True
                dfs(i+1)
                candidate.pop()
                used[i] = False

        dfs(0)
        return result
        
# @lc code=end

