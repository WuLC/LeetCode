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
        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                idx = stack.pop()
                if stack:
                    result = max(result, heights[idx] * (i - stack[-1] - 1))
                else:
                    result = max(result, heights[idx] * i)
            stack.append(i)
        
        # deal with increasing elements still in stack
        # including equal elements
        max_idx = stack[-1]
        while stack:
            idx = stack.pop()
            if stack:
                result = max(result, heights[idx] * (max_idx-stack[-1]))
            else:
                result = max(result, heights[idx] * (max_idx+1))
        return result
        
# @lc code=end

