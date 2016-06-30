# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-06-30 22:57:00
# @Last modified by:   WuLC
# @Last Modified time: 2016-06-30 22:57:15
# @Email: liangchaowu5@gmail.com

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