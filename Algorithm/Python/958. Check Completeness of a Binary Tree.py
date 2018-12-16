# -*- coding: utf-8 -*-
# Created on Sun Dec 16 2018 10:45:13
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# check level by level
class Solution(object):
    def isCompleteTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        curr = [root]
        missed = False
        while curr:
            next = []
            for node in curr:
                if (missed and (node.left or node.right)) or (node.left == None and node.right != None):
                    return False
                if node.left:
                    next.append(node.left)
                else:
                    missed = True
                if node.right:
                    next.append(node.right)
                else:
                    missed = True
            curr = next
        return True    