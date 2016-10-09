# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2016-08-19 17:40:54
# @Last modified by:   WuLC
# @Last Modified time: 2016-08-19 17:41:02
# @Email: liangchaowu5@gmail.com

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root==None: return 0
        left, right = root.left, root.right
        left_height, right_height = 0, 0 
        while left:
            left = left.left
            left_height += 1
        while right:
            right = right.right
            right_height += 1
        if left_height == right_height:
            return pow(2, left_height+1)-1
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)
        