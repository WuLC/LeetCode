#
# @lc app=leetcode id=42 lang=python
#
# [42] Trapping Rain Water
#

# @lc code=start
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        result, stack = 0, []
        for i, h in enumerate(height):
            while stack and height[stack[-1]] <= h:
                bottom = height[stack.pop()]
                if stack:
                    result += (min(h, height[stack[-1]]) - bottom) * (i - stack[-1] - 1)
            stack.append(i)
        return result

# @lc code=end
