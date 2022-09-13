#
# @lc app=leetcode id=139 lang=python
#
# [139] Word Break
#

# @lc code=start

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dp = [False] * (len(s)+1)
        dp[0] = True
        for i in range(len(s)):
            for w in wordDict:
                n = len(w)
                if i-n+1 >= 0 and dp[i-n+1] and s[i-n+1:i+1] == w:
                    dp[i+1] = True
                    break
        return dp[len(s)]


# # backtracking will TLE
# class Solution(object):
#     def wordBreak(self, s, wordDict):
#         """
#         :type s: str
#         :type wordDict: List[str]
#         :rtype: bool
#         """
#         def dfs(idx):
#             if idx == len(s):
#                 return True
#             for w in wordDict:
#                 end = idx+len(w)
#                 if end <= len(s) and s[idx:end] == w and dfs(idx+len(w)):
#                     return True
#             return False
#         return dfs(0)

        
# @lc code=end

