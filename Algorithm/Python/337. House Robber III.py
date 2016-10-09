# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-07-30 20:37:33
# @Last modified by:   WuLC
# @Last Modified time: 2016-07-30 20:41:13
# @Email: liangchaowu5@gmail.com

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return max(self.dfs(root))
    
    # return two value, the first represents the maximal money that can rob without robbing the root of the tree
    # the second represents the maximal money that can rob when robbing the root of the tree
    def dfs(self, root):
        if root == None:
            return (0,0)
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        return (max(left[1],left[0])+max(right[0],right[1]), root.val+left[0]+right[0])