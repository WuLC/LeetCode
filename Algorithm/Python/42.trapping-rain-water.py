#
# @lc app=leetcode id=42 lang=python
#
# [42] Trapping Rain Water
#

# @lc code=start

# calculate volumn of water in each column, O(n) time
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        maxRHeight = [0] * (n+1)
        for i in range(n-1, -1, -1):
            maxRHeight[i] = max(maxRHeight[i+1], height[i])

        result, curr_max = 0, height[0]
        for i in range(1, n-1):
            vol = min(curr_max, maxRHeight[i+1]) - height[i]
            if vol > 0:
                result += vol
            curr_max = max(curr_max, height[i])
        return result

        
# @lc code=end

