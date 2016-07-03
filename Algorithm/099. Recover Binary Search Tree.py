# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-07-03 20:01:22
# @Last modified by:   WuLC
# @Last Modified time: 2016-07-03 20:01:47
# @Email: liangchaowu5@gmail.com

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# O(n) space
class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        result, p1, p2= [], None, None
        self.inorderTraverse(root, result)
        for i in xrange(len(result)):
            if i+1<len(result) and result[i].val > result[i+1].val and p1 == None:
                p1 = result[i]
            elif i-1 >= 0 and result[i].val < result[i-1].val:
                p2 = result[i]
        if p1 and p2:
            p1.val, p2.val = p2.val, p1.val
            
    def inorderTraverse(self, root, result):
        if root == None: return
        self.inorderTraverse(root.left, result)
        result.append(root)
        self.inorderTraverse(root.right, result)
        