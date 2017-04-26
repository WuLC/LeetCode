# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2017-04-26 09:27:06
# @Last modified by:   WuLC
# @Last Modified time: 2017-04-26 09:27:18
# @Email: liangchaowu5@gmail.com

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# recursive
class Solution(object):
    
    def __init__(self):
        self.tilt = 0
        
        
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.tilt = 0
        self.treeSum(root)
        return self.tilt
        
        
    def treeSum(self, root):
        if root == None:
            return 0
        leftSum = self.treeSum(root.left)
        rightSum = self.treeSum(root.right)
        self.tilt += abs(leftSum - rightSum)
        return leftSum + rightSum + root.val
        