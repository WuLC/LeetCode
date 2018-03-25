# -*- coding: utf-8 -*-
# Created on Fri Mar 23 2018 17:3:14
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# serializing just returns the result of preorder traversal
# deserializing builds the result of inorder traversal from the result of preorder traversal, then build the tree with these two results
class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        # preorder traversal
        vals, stack = [], []
        curr = root
        while curr or len(stack)>0:
            if curr == None:
                curr = stack.pop().right
            else:
                vals.append(curr.val)
                stack.append(curr)
                curr = curr.left
        return ' '.join(map(str, vals))

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def build(pre, ino):
            if len(pre) == 0:
                return None
            val = pre[0]
            idx = ino.index(val)
            root = TreeNode(val)
            root.left = build(pre[1:1+idx], ino[:idx])
            root.right = build(pre[1+idx:], ino[idx+1:])
            return root
        preorder = map(int, data.split())
        inorder = sorted(preorder)
        return build(preorder, inorder)
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))