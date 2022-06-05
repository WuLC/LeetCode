#
# @lc app=leetcode id=450 lang=python
#
# [450] Delete Node in a BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if root == None:
            return root
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            if root.left == None:
                return root.right
            if root.right == None:
                return root.left
            
            # find smallest node in right subtree
            curr = root.right
            if curr.left == None:
                root.val = curr.val
                root.right = curr.right 
            else:
                while curr.left:
                    if curr.left.left == None:
                        root.val = curr.left.val
                        curr.left = curr.left.right
                        break
                    curr = curr.left
        return root
    
        
# @lc code=end

