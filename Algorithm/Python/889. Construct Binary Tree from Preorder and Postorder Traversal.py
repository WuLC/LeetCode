# -*- coding: utf-8 -*-
# Created on Sun Aug 19 2018 15:55:10
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# recursive
class Solution(object):
    def constructFromPrePost(self, pre, post):
        """
        :type pre: List[int]
        :type post: List[int]
        :rtype: TreeNode
        """
        if len(pre)==0:
            return None
        root = TreeNode(pre[0])
        s1, s2 = set(), set()
        idx = 0
        while idx < len(post)-1:
            s1.add(pre[idx+1])
            s2.add(post[idx])
            if s1==s2:
                break
            idx += 1
        root.left = self.constructFromPrePost(pre[1:idx+2], post[:idx+1])
        root.right = self.constructFromPrePost(pre[idx+2:], post[idx+1:-1])
        return root