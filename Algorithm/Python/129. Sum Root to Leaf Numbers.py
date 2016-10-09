# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-08-04 16:32:06
# @Last modified by:   WuLC
# @Last Modified time: 2016-08-04 16:32:24
# @Email: liangchaowu5@gmail.com

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        result = [0]
        if root!=None:
            self.helper(root, str(root.val), result)
        return result[0]
        
    def helper(self, root, tmp, result):
        if root.left == None and root.right == None:
            result[0] += int(tmp)
            return
        if root.left:
            self.helper(root.left, tmp+str(root.left.val), result)
        if root.right:
            self.helper(root.right, tmp+str(root.right.val), result)
        
        