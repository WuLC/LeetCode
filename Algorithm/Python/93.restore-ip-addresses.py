#
# @lc app=leetcode id=93 lang=python
#
# [93] Restore IP Addresses
#

# @lc code=start
class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        result, candidate = [], []

        def dfs(s, idx):
            if len(candidate) > 4:
                return
            if idx == len(s) and len(candidate) == 4:
                result.append('.'.join(candidate))
                return
            for i in range(idx, len(s)):
                if self.is_valid(s, idx, i+1):
                    candidate.append(s[idx:i+1])
                    dfs(s, i+1)
                    candidate.pop()
        
        dfs(s, 0)
        return result


    def is_valid(self, s, start, end):
        """check if s[start, end) is valid part"""
        if end - start > 3:
            return False
        if end - start > 1:
            return s[start] != '0' and int(s[start:end]) <= 255
        return True

# @lc code=end

