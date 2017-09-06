# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2017-09-06 12:47:58
# @Last Modified by:   WuLC
# @Last Modified time: 2017-09-06 23:19:43


# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# recursive 
# duplicate result for some cases like [2,2,2,3,null,3,null]
# Definition for a binary tree node.

class Solution(object):
    
    def __init__(self):
        self.result = []
        
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        self.result = []
        if root != None:
            self.helper(root.left, root.right)
        return self.result
    
    def helper(self, r1, r2):
        if r1 == None or r2 == None:
            return
        if r1.val == r2.val and self.isSame(r1, r2):
            self.result.append(r1)
        self.helper(r1, r2.left)
        self.helper(r1, r2.right)
        self.helper(r2, r1.left)
        self.helper(r2, r1.right)
    
    def isSame(self, r1, r2):
        if r1 == None and r2 == None:
            return True
        elif r1 == None or r2 == None:
            return False
        else:
            return r1.val == r2.val and r1.left == r2.left and r1.right == r2.right
  
# use a string to represent a tree
# the string is obtained by postorder traversal of the tree
class Solution(object):
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        result = []
        counter = {}
        self.preorder(root, counter, result)
        return result
    
    def preorder(self, root, counter, result):
        if root == None:
            return '#'
        curr = str(root.val) + ',' + self.preorder(root.left, counter, result) + ',' + self.preorder(root.right, counter, result)
        counter.setdefault(curr, 0)
        counter[curr] += 1
        if counter[curr] == 2:
            result.append(root)
        return curr