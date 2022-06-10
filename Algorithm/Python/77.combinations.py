#
# @lc app=leetcode id=77 lang=python
#
# [77] Combinations
#

# @lc code=start
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        result = []
        self.dfs(result, [], 1, n, k)
        return result
    
    def dfs(self, result, tmp, idx, n, k):
        if len(tmp) == k:
            result.append(tmp)
            return
        for i in range(idx, n+1):
            self.dfs(result, tmp+[i], i+1, n, k)
        
# @lc code=end

