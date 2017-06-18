# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2017-06-18 10:51:51
# @Last modified by:   LC
# @Last Modified time: 2017-06-18 10:52:13
# @Email: liangchaowu5@gmail.com

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def addOneRow(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """
        if d == 1:
            new_root = TreeNode(v)
            new_root.left = root
            return new_root
        
        count = 1
        curr_row = [root]
        while count < d-1:
            next_row = []
            for node in curr_row:
                if node.left != None:
                    next_row.append(node.left)
                if node.right != None:
                    next_row.append(node.right)
                curr_row = next_row
            count += 1
        
        for node in curr_row:
            new_left = TreeNode(v)
            new_right = TreeNode(v)
            new_left.left, new_right.right = node.left, node.right
            node.left, node.right = new_left, new_right 
        return root
        
        