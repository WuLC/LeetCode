# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-06-01 22:36:33
# @Last modified by:   WuLC
# @Last Modified time: 2016-06-03 23:05:49
# @Email: liangchaowu5@gmail.com


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# method 1,recursively
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        if root == None:
            return result
        result += self.postorderTraversal(root.left)
        result += self.postorderTraversal(root.right)
        result.append(root.val)
        return result


# method 2,iteratively
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack, result = [], []
        curr_node = root
        while len(stack)!=0 or curr_node != None:
            if curr_node != None:
                # result.insert(0, curr_node.val)
                result.append(curr_node.val)
                stack.append(curr_node)
                curr_node = curr_node.right
            else:
                tmp = stack.pop()
                curr_node = tmp.left
        result.reverse()
        return result