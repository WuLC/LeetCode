# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2017-08-08 20:21:04
# @Last Modified by:   WuLC
# @Last Modified time: 2017-08-08 20:21:20

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# recursive
class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums) == 0:
            return None
        index = nums.index(max(nums))
        root = TreeNode(nums[index])
        root.left = self.constructMaximumBinaryTree(nums[:index])
        root.right = self.constructMaximumBinaryTree(nums[index+1:])
        return root