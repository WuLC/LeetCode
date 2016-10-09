# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-08-30 10:49:12
# @Last modified by:   WuLC
# @Last Modified time: 2016-08-30 10:49:20
# @Email: liangchaowu5@gmail.com

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        if root == None:
            return []
        left = self.binaryTreePaths(root.left)
        right = self.binaryTreePaths(root.right)
        tmp = left+right
        if len(tmp) == 0:
            return [str(root.val)]
        else:
            return map(lambda x:str(root.val)+'->'+x, tmp)