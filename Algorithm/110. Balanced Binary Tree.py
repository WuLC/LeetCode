# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-08-01 12:02:49
# @Last modified by:   WuLC
# @Last Modified time: 2016-08-01 12:36:26
# @Email: liangchaowu5@gmail.com

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# method 1,from top to buttom, O(n^2)
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None: return True
        left = self.depth(root.left)
        right = self.depth(root.right)
        if abs(left-right) > 1:
            return False
        if self.isBalanced(root.left) and self.isBalanced(root.right):
            return True
        return False
    
    def depth(self, root):
        if root == None:
            return 0
        left = self.depth(root.left)
        right = self.depth(root.right)
        return max(left, right) + 1

# method 2, from buttom to top, O(n)
# -1 means that the tree of the node as root is not balanced
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.depth(root) != -1

    def depth(self, root):
        if root == None: return 0
        left = self.depth(root.left)
        right = self.depth(root.right)
        if left == -1 or right == -1 or abs(left - right) > 1:
            return -1
        return max(left, right)+1


