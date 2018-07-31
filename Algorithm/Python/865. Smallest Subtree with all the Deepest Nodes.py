# -*- coding: utf-8 -*-
# Created on Mon Jul 30 2018 23:26:44
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
    def subtreeWithAllDeepest(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        left, right = self.cal_depth(root.left), self.cal_depth(root.right)
        if left == right:
            return root
        elif left > right:
            return self.subtreeWithAllDeepest(root.left)
        else:
            return self.subtreeWithAllDeepest(root.right)
    
    def cal_depth(self, root):
        if root == None:
            return 0
        return 1 + max(self.cal_depth(root.left), self.cal_depth(root.right))


# more efficient recursive
# referer: https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/discuss/146808/One-pass
class Solution(object):
    def subtreeWithAllDeepest(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        left, right = self.cal_depth(root.left), self.cal_depth(root.right)
        if left == right:
            return root
        elif left > right:
            return self.subtreeWithAllDeepest(root.left)
        else:
            return self.subtreeWithAllDeepest(root.right)
    
    def cal_depth(self, root):
        if root == None:
            return (0, None)
        left, right = self.cal_depth(root.left), self.cal_depth(root.right)
        if left[0] == right[0]:
            return (left[0]+1, root)
        elif left[0] > right[0]:
            return (left[0]+1, left[1])
        else:
            return (right[0]+1, right[1])