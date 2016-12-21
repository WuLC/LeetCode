# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-12-21 21:16:46
# @Last modified by:   WuLC
# @Last Modified time: 2016-12-21 21:20:21
# @Email: liangchaowu5@gmail.com


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# long and naive solution
# find the node that has the same value as key
# delete it if it is a leaf, else replace it with the largest node on the left subtree or the smallest node on the right subtree
class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        dummy = TreeNode(0)
        dummy.left = root
        parent = dummy
        curr = root
        while curr and curr.val != key:
            parent = curr
            if curr.val > key:
                curr = curr.left
            else:
                curr = curr.right
        if curr != None: # find the node equal to the key
            if curr.left == None and curr.right == None:
                if parent.left and parent.left.val == key:
                    parent.left = None
                else:
                    parent.right = None
            else:
                self.modify(curr)
        return dummy.left
        
    def modify(self, root):
        if root.left:
            curr = root.left
            while curr.right and curr.right.right:
                curr = curr.right
            if curr.right:
                root.val = curr.right.val
                curr.right = curr.right.left
            else:
                root.val = curr.val
                root.left = curr.left
        else:
            curr = root.right
            while curr.left and curr.left.left:
                curr = curr.left
            if curr.left:
                root.val = curr.left.val
                curr.left = curr.left.right
            else:
                root.val = curr.val
                root.right = curr.right