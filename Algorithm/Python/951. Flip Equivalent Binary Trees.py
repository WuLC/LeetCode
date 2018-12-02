# -*- coding: utf-8 -*-
# Created on Sun Dec 02 2018 19:19:40
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# simple recursive
class Solution(object):
    def flipEquiv(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        if root1 == None and root2 == None:
            return True
        elif root1 == None or root2 == None:
            return False
        else:
            return root1.val == root2.val and\
                   ((self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right)) or\
                    (self.flipEquiv(root1.left, root2.right) and self.flipEquiv(root1.right, root2.left)))