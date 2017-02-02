# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2017-02-02 13:01:21
# @Last modified by:   WuLC
# @Last Modified time: 2017-02-02 13:02:16
# @Email: liangchaowu5@gmail.com

# traverse the tree and get the most frequently occurred element

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None: return []
        count = collections.defaultdict(int)
        curr = root
        nodes = []
        while curr or nodes:
            if curr:
                count[curr.val] += 1
                nodes.append(curr)
                curr = curr.left
            else:
                curr = nodes.pop().right 
        max_num = max(count.values()) # max() can deal with empty list
        return [k for k,v in count.items() if v == max_num]
        