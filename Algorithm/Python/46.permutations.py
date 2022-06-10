#
# @lc app=leetcode id=46 lang=python
#
# [46] Permutations
#

# @lc code=start
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result, tmp, used = [], [], [False]*len(nums)

        def dfs():
            if len(tmp) == len(nums):
                result.append(tmp[:])
                return
            for i in range(len(nums)):
                if not used[i]:
                    tmp.append(nums[i])
                    used[i] = True
                    dfs()
                    used[i] = False
                    tmp.pop()

        dfs()
        return result
        
# @lc code=end

