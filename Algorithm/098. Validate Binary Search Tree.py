# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-06-08 19:50:52
# @Last modified by:   WuLC
# @Last Modified time: 2016-06-08 19:51:06
# @Email: liangchaowu5@gmail.com

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        result = self.inorderTra(root)
        for i in xrange(1,len(result)):
            if result[i] <= result[i-1]:
                return False
        return True
        
    def inorderTra(self,root):
        result = []
        if root == None:
            return result
        result += self.inorderTra(root.left)
        result.append(root.val)
        result += self.inorderTra(root.right)
        return result   