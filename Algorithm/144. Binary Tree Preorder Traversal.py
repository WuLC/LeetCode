# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-06-01 22:24:37
# @Last modified by:   WuLC
# @Last Modified time: 2016-06-01 22:34:46
# @Email: liangchaowu5@gmail.com


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# method 1,recursively
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        if root == None:
            return result
        result.append(root.val)
        result += self.preorderTraversal(root.left)
        result += self.preorderTraversal(root.right)
        return result
            
# method 2,iteratively
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack, result = [], []
        curr_node = root
        while len(stack) != 0 or curr_node!= None:
            if curr_node != None:
                result.append(curr_node.val)
                stack.append(curr_node)
                curr_node = curr_node.left
            else:
                tmp = stack.pop()
                curr_node = tmp.right
        return result       