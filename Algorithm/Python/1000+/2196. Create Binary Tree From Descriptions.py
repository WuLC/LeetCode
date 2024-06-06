# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def createBinaryTree(self, descriptions):
        """
        :type descriptions: List[List[int]]
        :rtype: Optional[TreeNode]
        """
        record, child2parent = {} , {}
        for parent, child, is_left in descriptions:
            if parent not in record:
                record[parent] = TreeNode(parent, None, None)
            if child not in record:
                record[child] = TreeNode(child, None, None)

            if is_left:
                record[parent].left = record[child]
            else:
                record[parent].right = record[child]
            child2parent[child] = parent
        
        root = None
        for p, _, _ in descriptions:
            if p not in child2parent:
                root = record[p]
                break
        return root
            
