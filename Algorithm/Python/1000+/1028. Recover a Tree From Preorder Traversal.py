# -*- coding: utf-8 -*-
# Created on Sun Apr 14 2019 16:4:54
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# stack
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# stack, two pointers
# referer: https://leetcode.com/problems/recover-a-tree-from-preorder-traversal/discuss/274605/C%2B%2B-Iterative-Stack
class Solution(object):
    def recoverFromPreorder(self, S):
        """
        :type S: str
        :rtype: TreeNode
        """
        p1, p2, stack = 0, 0, []
        while p1 < len(S):
            level = 0
            while S[p1] == '-':
                p1 += 1
                p2 += 2
                level += 1
            while p2 < len(S) and S[p2] != '-':
                p2 += 1
            while stack and len(stack) > level:
                stack.pop()
            curr_node = TreeNode(int(S[p1 : p2]))
            if stack:
                if stack and stack[-1].left == None:
                    stack[-1].left = curr_node
                else:
                    stack[-1].right = curr_node
            stack.append(curr_node)
            p1 = p2
        return stack[0]




# recursive with regex do not work as it can not identify a--b--c as a--b and b--c
# import re
# class Solution(object):
#     def recoverFromPreorder(self, S):
#         """
#         :type S: str
#         :rtype: TreeNode
#         """
#         return self.dfs(1, S)

#     def dfs(self, level, s):
#         if len(s) == 0:
#             return None
#         mark, p1 = '\d+' + '-'*level + '\d+', []
#         for m in re.finditer(mark, s):
#             i = m.start()
#             while s[i].isdigit():
#                 i += 1
#             p1.append(i)
#         if len(p1) == 0:
#             return TreeNode(int(s))
#         root = TreeNode(int(s[:p1[0]]))
#         if len(p1) == 2:
#             root.left = self.dfs(level + 1, s[p1[0] + level:p1[1]])
#             root.right = self.dfs(level + 1, s[p1[1] + level:])
#         else:
#             root.left = self.dfs(level + 1, s[p1[0] + level:])
#         return root

