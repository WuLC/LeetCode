#
# @lc app=leetcode id=1047 lang=python
#
# [1047] Remove All Adjacent Duplicates In String
#

# @lc code=start
class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        for c in s:
            if stack and stack[-1] == c:
                stack.pop()
            else:
                stack.append(c)
        return ''.join(stack)

        
# @lc code=end

