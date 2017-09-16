# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2017-09-16 22:07:15
# @Last Modified by:   WuLC
# @Last Modified time: 2017-09-16 22:14:53

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


# 