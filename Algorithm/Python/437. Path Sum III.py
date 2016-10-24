# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-10-24 23:16:16
# @Last modified by:   WuLC
# @Last Modified time: 2016-10-24 23:19:03
# @Email: liangchaowu5@gmail.com


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None



# discuss the two cases when root is included or not
class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        return 0 if root == None else self.pathSum(root.left, sum) + self.pathSum(root.right, sum) + self.with_root(root, sum)
        
    def with_root(self, root, sum):
        if root == None:
            return 0
        elif root.val == sum:
            return 1 + self.with_root(root.left, 0) + self.with_root(root.right, 0)
        else:
            return self.with_root(root.left, sum-root.val) + self.with_root(root.right, sum-root.val)
        
            
        
            