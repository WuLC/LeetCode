#
# @lc app=leetcode id=40 lang=python
#
# [40] Combination Sum II
#

# @lc code=start
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        result, tmp, used = [], [], [False] * len(candidates)


        def dfs(idx, curr_sum):
            if curr_sum >= target:
                if curr_sum == target:
                    result.append(tmp[:])
                return
            
            for i in range(idx, len(candidates)):
                if i > 0 and candidates[i] == candidates[i-1] and used[i-1] == False:
                    continue
                tmp.append(candidates[i])
                used[i] = True
                dfs(i+1, curr_sum + candidates[i])
                used[i] = False
                tmp.pop()

        dfs(0, 0)        
        return result


# @lc code=end

