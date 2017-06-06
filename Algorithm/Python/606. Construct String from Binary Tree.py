# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2017-06-06 16:11:17
# @Last modified by:   WuLC
# @Last Modified time: 2017-06-06 16:11:30
# @Email: liangchaowu5@gmail.com

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None



# recursive
class Solution(object):
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        s = self.helper(t)
        return s[1:-1]
        
    
    def helper(self, root):
        if root == None:
            return '()'
        left = self.helper(root.left)
        right = self.helper(root.right)
        if right == '()':
            content = str(root.val) if left == '()' else str(root.val) + left
        else:
            content = str(root.val) + left + right
        return '(' + content + ')'