# -*- coding: utf-8 -*-
# Created on Tue Dec 05 2017 10:17:33
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# union find set
class Solution(object):
    def areSentencesSimilarTwo(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        if len(words1) != len(words2):
            return False
        # construct union find set
        self.parents = {}
        for pair in pairs:
            if pair[0] not in self.parents:
                self.parents[pair[0]] = pair[0]
            if pair[1] not in self.parents:
                self.parents[pair[1]] = pair[1]
        for pair in pairs:
            self.union(pair[0], pair[1])
        
        # perform union find
        for i in xrange(len(words1)):
            if words1[i] == words2[i]:
                continue
            elif words1[i] not in self.parents or words2[i] not in self.parents:
                return False
            elif self.find(words1[i]) != self.find(words2[i]):
                return False
        return True
        
        
    def find(self, word):
        if self.parents[word] != word:
            p = self.find(self.parents[self.parents[word]])
            self.parents[word] = p
        return self.parents[word]
    
    
    def union(self, w1, w2):
        p1 = self.find(w1)
        p2 = self.find(w2)
        if p1 != p2:
            self.parents[p2] = p1


# based on the above solution, add union by rank
class Solution(object):
    def areSentencesSimilarTwo(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        if len(words1) != len(words2):
            return False
        # construct union find set
        self.parents = {}
        self.rank = {}
        for pair in pairs:
            if pair[0] not in self.parents:
                self.parents[pair[0]] = pair[0]
                self.rank[pair[0]] = 0
            if pair[1] not in self.parents:
                self.parents[pair[1]] = pair[1]
                self.rank[pair[1]] = 0
        for pair in pairs:
            self.union(pair[0], pair[1])
        
        # perform union find
        for i in xrange(len(words1)):
            if words1[i] == words2[i]:
                continue
            elif words1[i] not in self.parents or words2[i] not in self.parents:
                return False
            elif self.find(words1[i]) != self.find(words2[i]):
                return False
        return True
        
        
    def find(self, word):
        if self.parents[word] != word:
            p = self.find(self.parents[self.parents[word]])
            self.parents[word] = p
        return self.parents[word]
    
    
    def union(self, w1, w2):
        p1 = self.find(w1)
        p2 = self.find(w2)
        if p1 != p2:
            if self.rank[p1] > self.rank[p2]:
                self.parents[p2] = p1
            elif self.rank[p1] < self.rank[p2]:
                self.parents[p1] = p2
            else:
                self.parents[p2] = p1
                self.rank[p1] += 1
        