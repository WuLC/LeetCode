# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2016-07-30 10:17:32
# @Last modified by:   WuLC
# @Last Modified time: 2016-07-30 10:17:40
# @Email: liangchaowu5@gmail.com

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root == None: return '#'
        curr_level = [root]
        result = []
        while curr_level:
            tmp, next_level = [], []
            for i in xrange(len(curr_level)):
                if curr_level[i] == '#':
                    tmp.append('#')
                else:
                    tmp.append(str(curr_level[i].val))
                    if curr_level[i].left:
                        next_level.append(curr_level[i].left)
                    else:
                        next_level.append('#')
                    if curr_level[i].right:
                        next_level.append(curr_level[i].right)
                    else:
                        next_level.append('#')
            result.append(','.join(tmp))
            curr_level = next_level
        return '%'.join(result)
                    
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == '#': return None
        levels = [level.split(',') for level in data.split('%')]
        pre_level = []
        for i in xrange(len(levels)):
            curr_level = []
            if i==0:
                root = TreeNode(int(levels[i][0]))
                curr_level.append(root)
            else:
                for j in xrange(len(pre_level)):
                    if levels[i][j*2]=='#':
                        pre_level[j].left = None
                    else:
                        tmp = TreeNode(int(levels[i][j*2]))
                        pre_level[j].left = tmp
                        curr_level.append(tmp)
                    if levels[i][j*2+1]=='#':
                        pre_level[j].right = None
                    else:
                        tmp = TreeNode(int(levels[i][j*2+1]))
                        pre_level[j].right = tmp
                        curr_level.append(tmp)
            pre_level = curr_level
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))