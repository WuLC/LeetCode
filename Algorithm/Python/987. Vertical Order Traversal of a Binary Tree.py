# -*- coding: utf-8 -*-
# Created on Mon Feb 04 2019 14:37:43
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# hashtable with priority queue
from heapq import heappush, heappop

class Solution(object):
    def verticalTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        index = {}
        self.dfs(root, 0, 0, index)
        result = []
        for k, v in sorted(index.items()):
            tmp = []
            while len(v) > 0:
                tmp.append(heappop(v)[1])
            result.append(tmp)
        return result
        
    
    def dfs(self, root, x, y, index):
        if root == None:
            return
        if x not in index:
            index[x] = []
        heappush(index[x], (-y, root.val))
        self.dfs(root.left, x-1, y-1, index)
        self.dfs(root.right, x+1, y-1, index)