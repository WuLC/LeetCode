# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2017-03-24 23:59:51
# @Last modified by:   WuLC
# @Last Modified time: 2017-03-25 00:00:09
# @Email: liangchaowu5@gmail.com

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# recursive 
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        height = 0
        if root.left:
            height += (self.get_height(root.left)+1)
        if root.right:
            height += (self.get_height(root.right)+1)
        return max(self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right), height)
    
    def get_height(self, root):
        if root == None:
            return 0
        tmp = max(self.get_height(root.left), self.get_height(root.right))
        return tmp+1 if root.left or root.right else 0