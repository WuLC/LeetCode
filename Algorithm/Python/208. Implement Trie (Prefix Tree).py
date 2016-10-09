# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2016-07-13 09:40:04
# @Last modified by:   WuLC
# @Last Modified time: 2016-07-13 09:40:12
# @Email: liangchaowu5@gmail.com

class TrieNode(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.val = ''
        self.childs = {}

class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        tmp = self.root
        for s in word:
            if s not in tmp.childs:
                node = TrieNode()
                node.val = s
                tmp.childs[s] = node
            tmp = tmp.childs[s]
        tmp.childs[''] = TrieNode()
            
        

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        tmp = self.root
        for s in word:
            if s in tmp.childs:
                tmp = tmp.childs[s]
                continue
            else:
                return False
        if '' in tmp.childs:
            return True
        else:
            return False
        

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie
        that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        tmp = self.root
        for s in prefix:
            if s in tmp.childs:
                tmp = tmp.childs[s]
                continue
            return False
        return True
        
        

# Your Trie object will be instantiated and called as such:
# trie = Trie()
# trie.insert("somestring")
# trie.search("key")