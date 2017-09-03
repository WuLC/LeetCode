# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2017-09-03 10:27:46
# @Last Modified by:   WuLC
# @Last Modified time: 2017-09-03 10:28:46

# find the node whose value is exactly larger than the value of root 

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return -1
        curr = [root]
        result = -1
        while curr:
            next = []
            for node in curr:
                if node.left:
                    next.append(node.left)
                    next.append(node.right)
                if node.val != root.val:
                    result = min(result, node.val) if result != -1 else node.val
            curr = next
        return result
            
        