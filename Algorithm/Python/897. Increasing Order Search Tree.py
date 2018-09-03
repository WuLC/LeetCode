# -*- coding: utf-8 -*-
# Created on Mon Sep 03 2018 11:32:50
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# recursive
class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root == None:
            return None
        if root.left != None:
            new_root = self.increasingBST(root.left)
            tmp = new_root
            while tmp.right:
                tmp = tmp.right
            root.left = None
            tmp.right = root
        else:
            new_root = root
        root.right = self.increasingBST(root.right) 
        return new_root