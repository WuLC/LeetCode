# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2016-05-31 10:15:31
# @Last modified by:   WuLC
# @Last Modified time: 2016-06-03 22:47:24
# @Email: liangchaowu5@gmail.com

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None



# method 1,recursively
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        if root == None:
            return result
        result += self.inorderTraversal(root.left)
        result.append(root.val)
        result += self.inorderTraversal(root.right)
        return result


# method 2,iteratively     
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack, result= [], []
        curr_node = root
        while len(stack) != 0 or curr_node != None:
            if curr_node != None:
                stack.append(curr_node)
                curr_node = curr_node.left
            else:
                tmp = stack.pop()
                result.append(tmp.val)
                curr_node = tmp.right
        return result