# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2017-09-16 22:07:15
# @Last Modified by:   WuLC
# @Last Modified time: 2017-09-30 15:39:43

# hashmap, compare words with same length
class MagicDictionary(object):

    def buildDict(self, dict):
        """Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: void
        """
        self.mapping = {}
        for word in dict:
            n = len(word)
            self.mapping.setdefault(n, list())
            self.mapping[n].append(word)
        
    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        """
        if len(word) not in self.mapping:
            return False
        for w in self.mapping[len(word)]:
            count = 0
            for i in xrange(len(word)):
                if w[i] != word[i]:
                    count += 1
            if count == 1:
                return True
        return False


# Trie
# the most important part is to search in the trie with at most one change
class TrieNode():
    def __init__(self):
        self.next = [None] * 26
        self.isWord = False
        
class MagicDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        

    def buildDict(self, dict):
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: void
        """
        for word in dict:
            curr = self.root
            for char in word:
                idx = ord(char) - ord('a')
                if curr.next[idx] == None:
                    curr.next[idx] = TrieNode()
                curr = curr.next[idx]
            curr.isWord = True
        
            
                
    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        """
        def helper(root, word, idx, count):
            if count > 1:
                return False
            root_idx = ord(word[idx]) - ord('a')
            if len(word) - 1 == idx:
                if count == 1:
                    return root.next[root_idx] and root.next[root_idx].isWord
                else: # count  = 0
                    return any([root.next[i] and root.next[i].isWord for i in xrange(26) if i != root_idx])               
            for i in xrange(26):
                if root.next[i]:
                    if (i == root_idx and helper(root.next[i], word, idx + 1, count)) or \
                       (i != root_idx and helper(root.next[i], word, idx + 1, count + 1)):
                        return True
            return False
        
        return helper(self.root, word, 0, 0)
                   