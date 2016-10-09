# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-06-30 22:57:00
# @Last modified by:   WuLC
# @Last Modified time: 2016-09-26 22:50:27
# @Email: liangchaowu5@gmail.com


# method 1, store words in a hashmap in terms of their length, AC
# beat 98.16%
class WordDictionary(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.words = {}
        

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        n = len(word)
        if n not in self.words:
            self.words[n] = []
        self.words[n].append(word)
        

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could
        contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        n = len(word)
        if n not in self.words:
            return False
        candidates = self.words[n]
        for can in candidates:
            for i in xrange(n):
                if word[i] == '.' or can[i] == word[i]:
                    if i == n-1:
                        return True
                    continue
                else:
                    break
        return False



# method 2, implement with Trie
# beat 10%
class TrieNode:
    def __init__(self):
        self.word = False
        self.children = {}

class WordDictionary(object):
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.word = True
                

    def search(self, word):
        def helper(root, word):
            if len(word) == 0  and root.word == True:
                return True
            curr = root
            for i in xrange(len(word)):
                if word[i] == '.':
                    next = curr.children.values()
                elif word[i] in curr.children:
                    next = [curr.children[word[i]]]
                else:
                    return False
                return any([helper(node, word[i+1:]) for node in next])
        return helper(self.root, word)

# change helper  function 
# manner 1, beat 23%
def helper(root, word):
    if len(word) == 0:
        return root.word == True
    if word[0] == '.':
        next = root.children.values()
    elif word[0] in root.children:
        next = [root.children[word[0]]]
    else:
        return False
    return any([helper(node, word[1:]) for node in next])

# manner 2, 778 ms, beat 58.9%
def helper(root, word):
    if len(word) == 0:
        return root.word == True
    if word[0] != '.':
        return word[0] in root.children and helper(root.children[word[0]], word[1:])
    return any([helper(node, word[1:]) for node in root.children.values()])


# method 3, same idea as method 2
# but need not to implement the Trie class
class WordDictionary(object):
    def __init__(self):
        self.root = {}
        

    def addWord(self, word):
        curr = self.root
        for char in word:
            curr.setdefault(char, {})
            curr = curr[char]
        curr['#'] = '#'  # specify it as a word
            
    def search(self, word):
        def find(root, word):
            if len(word) == 0:
                return '#' in root
            if word[0] != '.':
                return word[0] in root and find(root[word[0]], word[1:])
            return any([find(node, word[1:]) for node in root.values() if node != '#']) # pay attention a word has no children 
        return find(self.root, word)