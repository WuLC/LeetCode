#
# @lc app=leetcode id=84 lang=python
#
# [84] Largest Rectangle in Histogram
#

# @lc code=start
class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        result, stack = 0, []
        heights = [0] + heights + [0]
        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                curr_height = heights[stack.pop()]
                result = max(result, curr_height * (i - stack[-1] - 1))
            stack.append(i)
        return result
        
# @lc code=end

