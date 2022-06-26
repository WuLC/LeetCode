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
        result, tmp = [], []
        def dfs(idx, s):
            if idx == len(s):
                result.append(tmp[:])
                return
            for i in range(idx, len(s)):
                if self.isPalindorme(idx, i, s):
                    tmp.append(s[idx:i+1])
                    dfs(i+1, s)
                    tmp.pop()
        
        dfs(0, s)
        return result
    
    def isPalindorme(self, start, end, s):
        while start < end:
            if s[start] != s[end]:
                return False
            start, end = start+1, end-1
        return True

# @lc code=end

