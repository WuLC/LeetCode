#
# @lc app=leetcode id=39 lang=python
#
# [39] Combination Sum
#

# @lc code=start
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result, tmp = [], []
    
        def dfs(idx, curr_sum):
            if curr_sum >= target:
                if curr_sum == target:
                    result.append(tmp[:])
                return
            for i in range(idx, len(candidates)):
                tmp.append(candidates[i])
                dfs(i, curr_sum + candidates[i])
                tmp.pop()
        
        dfs(0, 0)
        return result

# @lc code=end

