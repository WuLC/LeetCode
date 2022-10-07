#
# @lc app=leetcode id=131 lang=python
#
# [131] Palindrome Partitioning
#

# @lc code=start
class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        result, n = [], len(s)
        dp = [[False]*n for _ in range(n)]
        for i in range(n-1, -1, -1):
            for j in range(i, n, 1):
                if i == j:
                    dp[i][j] = True
                elif s[i] == s[j] and (i+1 >= j-1 or dp[i+1][j-1]):
                    dp[i][j] = True
        
        def dfs(idx, tmp):
            if idx == n:
                result.append(tmp[:])
                return
            for i in range(idx, n):
                if dp[idx][i]:
                    tmp.append(s[idx:i+1])
                    dfs(i+1, tmp)
                    tmp.pop()
        
        dfs(0, [])
        return result



# @lc code=end

