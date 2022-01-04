#
# @lc app=leetcode id=496 lang=python
#
# [496] Next Greater Element I
#

# @lc code=start
class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        result = [-1] * len(nums1)
        num2idx = {nums1[i]:i for i in range(len(nums1))}
        stack = []
        for num in nums2:
            while stack and stack[-1] < num:
                if stack[-1] in num2idx:
                    result[num2idx[stack[-1]]] = num
                stack.pop()
            stack.append(num)
        return result
        
# @lc code=end

