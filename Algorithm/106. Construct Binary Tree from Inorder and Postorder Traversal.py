# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-07-01 20:43:17
# @Last modified by:   WuLC
# @Last Modified time: 2016-07-01 20:43:26
# @Email: liangchaowu5@gmail.com

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        return self.helper(inorder, 0, len(inorder)-1, postorder, 0, len(postorder)-1)
        
    def helper(self, inorder, ileft, iright, postorder, pleft, pright):
        if ileft > iright: return None
        if ileft == iright: return TreeNode(inorder[ileft])
        inx = inorder.index(postorder[pright])
        left_len = inx - ileft
        root = TreeNode(postorder[pright])
        root.left = self.helper(inorder, ileft, inx-1, postorder, pleft, pleft+left_len-1) 
        root.right = self.helper(inorder, inx+1, iright, postorder, pleft+left_len, pright-1)
        return root