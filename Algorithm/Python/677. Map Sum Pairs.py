# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2017-09-22 09:12:45
# @Last Modified by:   WuLC
# @Last Modified time: 2017-09-22 09:14:36

# Trie
class TrieNode():
    def __init__(self, cnt):
        self.count = cnt
        self.next = {}
        
        
        
class MapSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode(0)
        

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        curr = self.root
        for c in key:
            if c not in curr.next:
                curr.next[c] = TrieNode(0)
            curr = curr.next[c]
        curr.count = val
                

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        curr = self.root
        for c in prefix:
            if c in curr.next:
                curr = curr.next[c]
            else:
                return 0
        return self.addup(curr)
    
    
    def addup(self, root):
        result = root.count
        for char, node in root.next.items():
            result += self.addup(node)
        return result
        
        
            


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)