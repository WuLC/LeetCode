# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2016-07-16 09:02:25
# @Last modified by:   WuLC
# @Last Modified time: 2016-07-16 09:34:54
# @Email: liangchaowu5@gmail.com

# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# method 1, O(n) space
class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.curr_node = root
        self.stack = []
        self.values = []
        while len(self.stack)>0 or self.curr_node:
            if self.curr_node:
                self.stack.append(self.curr_node)
                self.curr_node = self.curr_node.left
            else:
                self.curr_node = self.stack.pop()
                self.values.append(self.curr_node.val)
                self.curr_node = self.curr_node.right
        self.values.reverse()
            
        
    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.values)>0 

    def next(self):
        """
        :rtype: int
        """
        return self.values.pop()
        

# method 2, O(h) space
class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        self.curr = root
        
    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.stack)>0 or self.curr

    def next(self):
        """
        :rtype: int
        """
        while self.curr:
            self.stack.append(self.curr)
            self.curr = self.curr.left
        tmp = self.stack.pop()
        self.curr = tmp.right
        return tmp.val