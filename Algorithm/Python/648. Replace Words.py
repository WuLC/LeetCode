# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2017-07-26 21:57:12
# @Last modified by:   LC
# @Last Modified time: 2017-07-26 21:57:31
# @Email: liangchaowu5@gmail.com


# Trie
class TrieNode:
    def __init__(self):
        self.next = [None for _ in xrange(26)]
        self.isRoot = False


class Solution(object):
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        root = TrieNode()
        # build the trie
        for word in dict:
            curr = root
            for c in word:
                idx = ord(c) - 97
                if curr.next[idx] == None:
                    curr.next[idx] = TrieNode()
                curr = curr.next[idx]
            curr.isRoot = True
        
        # replace all the successor 
        sentence = sentence.split()
        for i in xrange(len(sentence)):
            word = sentence[i]
            curr = root
            for j in xrange(len(word)):
                idx = ord(word[j]) - 97
                curr = curr.next[idx]
                if curr == None:
                    break
                if curr.isRoot:
                    sentence[i] = word[:j+1]
                    break
        return ' '.join(sentence)
                    