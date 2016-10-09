# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-06-14 14:42:14
# @Last modified by:   WuLC
# @Last Modified time: 2016-06-14 14:42:22
# @Email: liangchaowu5@gmail.com

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None: return []
        nodes, result= [root], []
        while len(nodes) > 0:
            next_level, tmp = [], []
            for i in xrange(len(nodes)):
                tmp.append(nodes[i].val)
                if nodes[i].left:
                    next_level.append(nodes[i].left)
                if nodes[i].right:
                    next_level.append(nodes[i].right)
            result.append(tmp)
            nodes = next_level
        r = []
        while len(result)>0:
            r.append(result.pop())
        return r