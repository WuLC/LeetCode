# -*- coding: utf-8 -*-
# Created on Mon Oct 08 2018 14:24:45
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# simple solution, record the last two rows
class CBTInserter(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.root = root
        self.curr, self.next, self.idx = [], [root], 0
        end = False
        while not end:
            self.curr = self.next
            self.next = []
            for i in xrange(len(self.curr)):
                if self.curr[i].left:
                    self.next.append(self.curr[i].left)
                else:
                    self.idx = i
                    end = True
                    break
                if self.curr[i].right:
                    self.next.append(self.curr[i].right)
                else:
                    self.idx = i
                    end = True
                    break

    def insert(self, v):
        """
        :type v: int
        :rtype: int
        """
        if self.curr[-1].right and self.idx == len(self.curr) - 1:
            self.curr = self.next
            self.next = []
            self.idx = 0
        node = TreeNode(v)
        if self.curr[self.idx].left == None:
            self.curr[self.idx].left = node
        elif self.curr[self.idx].right == None:
            self.curr[self.idx].right = node
        else:
            self.idx += 1
            self.curr[self.idx].left = node
        self.next.append(node)
        return self.curr[self.idx].val
        
    def get_root(self):
        """
        :rtype: TreeNode
        """
        return self.root


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(v)
# param_2 = obj.get_root()