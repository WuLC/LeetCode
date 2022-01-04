#
# @lc app=leetcode id=503 lang=python
#
# [503] Next Greater Element II
#

# @lc code=start
class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = [-1] * len(nums)
        stack = []
        for _ in range(2):
            for i, num in enumerate(nums):
                while stack and nums[stack[-1]] < num:
                    idx = stack.pop()
                    if result[idx] == -1:
                        result[idx] = num
                stack.append(i)
        return result
        
# @lc code=end

