# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-07-14 20:15:30
# @Last modified by:   WuLC
# @Last Modified time: 2016-07-14 20:30:09
# @Email: liangchaowu5@gmail.com

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# TLE
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if self.is_node(root.left, p, q):
            return self.lowestCommonAncestor(root.left, p, q)
        elif self.is_node(root.right, p, q):
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root
        
    def is_node(self, root, p1, p2):
        if root == None:
            return False
        r1, r2 = False, False
        stack,curr_node = [], root
        while len(stack) > 0 or curr_node != None:
            if curr_node:
                if p1 == curr_node: r1 = True 
                if p2 == curr_node: r2 = True 
                if r1 and r2:
                    return True
                stack.append(curr_node)
                curr_node = curr_node.left
            else:
                curr_node = stack.pop().right
        return False

# AC
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root == q or root == p or root == None: # if root in (None, p, q):
            return root
        left, right = self.lowestCommonAncestor(root.left, p, q), self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        elif left:
            return left
        else:
            return right