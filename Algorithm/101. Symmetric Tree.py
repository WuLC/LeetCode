# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-06-14 14:10:33
# @Last modified by:   WuLC
# @Last Modified time: 2016-06-14 14:10:44
# @Email: liangchaowu5@gmail.com

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None: return True
        left, right = [], []
        # left_tree
        stack, curr_node = [], root.left
        while len(stack) > 0 or curr_node != None:
            if curr_node != None:
                left.append(curr_node.val)
                stack.append(curr_node)
                curr_node = curr_node.left
            else:
                tmp = stack.pop()
                if tmp.right != None:
                    left.append(None)
                curr_node = tmp.right
                
        # right_tree
        stack, curr_node = [], root.right
        while len(stack) > 0 or curr_node != None:
            if curr_node != None:
                right.append(curr_node.val)
                stack.append(curr_node)
                curr_node = curr_node.right
            else:
                tmp = stack.pop()
                if tmp.left != None:
                    right.append(None)
                curr_node = tmp.left
        
        return left == right