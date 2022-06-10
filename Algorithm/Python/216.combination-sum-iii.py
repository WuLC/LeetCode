#
# @lc app=leetcode id=216 lang=python
#
# [216] Combination Sum III
#

# @lc code=start


class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        result, tmp = [], []
        self.dfs(result, tmp, 0, 1, k, n)
        return result

    def dfs(self, result, tmp, curr_sum, idx, k, n):
        if len(tmp) == k:
            if curr_sum == n:
                result.append(copy.deepcopy(tmp))
            return
        for i in range(idx, 10):
            tmp.append(i)
            self.dfs(result, tmp, curr_sum + i, i + 1, k, n)
            tmp.pop()
        
# @lc code=end

