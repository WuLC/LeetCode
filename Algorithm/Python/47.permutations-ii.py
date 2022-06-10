#
# @lc app=leetcode id=47 lang=python
#
# [47] Permutations II
#

# @lc code=start
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result, tmp, used = [], [], [False] * len(nums)
        nums.sort()

        def dfs(idx):
            if idx > 0 and nums[idx] == nums[idx-1] and used[idx-1] == False:
                return
            if len(tmp) == len(nums):
                result.append(tmp[:])
                return
            for i in range(len(nums)):
                if not used[i]:
                    tmp.append(nums[i])
                    used[i] = True
                    dfs(i)
                    used[i] = False
                    tmp.pop()

        dfs(0)
        return result

# @lc code=end

