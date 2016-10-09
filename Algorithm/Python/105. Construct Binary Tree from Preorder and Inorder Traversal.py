# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-07-01 19:33:31
# @Last modified by:   WuLC
# @Last Modified time: 2016-07-01 20:25:36
# @Email: liangchaowu5@gmail.com

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None




# slicing will lead to MLE, like the following code
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        n = len(preorder)
        if n==0:
            return None
        if n == 1:
            return TreeNode(preorder[0])
        root = ListNode(preorder[0])
        for i in xrange(n):
            if inorder[i] == root.val:
                left_nodes = i 
        left = self.buildTree(preorder[1:1+left_nodes], inorder[:left_nodes])
        right = self.buildTree(preorder[1+left_nodes:], inorder[left_nodes+1:])
        root.left, root.right = left, right
        return root

# to avoid MLE, build a helper function use index instead of slicing                
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        return self.helper(preorder, 0, len(preorder)-1, inorder, 0, len(inorder)-1)

    def helper(self, preorder, pleft, pright, inorder, ileft, iright):
        if pleft > pright:
            return None
        if pleft == pright:
            return TreeNode(preorder[pleft])
        inx = inorder.index(preorder[pleft])
        left_len = inx - ileft
        root = TreeNode(preorder[pleft])
        root.left = self.helper(preorder, pleft + 1, pleft + left_len, inorder, ileft, inx-1)
        root.right = self.helper(preorder, pleft + left_len + 1, pright, inorder, inx+1, right)
        return root


                