# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-07-03 11:27:48
# @Last modified by:   WuLC
# @Last Modified time: 2016-07-03 11:27:58
# @Email: liangchaowu5@gmail.com

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums) == 0: return None
        return self.helper(nums, 0, len(nums)-1)
        
    def helper(self, nums, left, right):
        if left > right:
            return
        if left == right:
            return TreeNode(nums[left])
        mid = (left+right)/2
        root = TreeNode(nums[mid])
        root.left = self.helper(nums, left, mid-1)
        root.right = self.helper(nums, mid+1, right)
        return root
        