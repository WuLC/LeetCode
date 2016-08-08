# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-08-07 15:47:20
# @Last modified by:   WuLC
# @Last Modified time: 2016-08-08 12:56:24
# @Email: liangchaowu5@gmail.com


# method 1, BFS, TLE, O(k*n^2), k refers to the lenght of  each word
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """
        distance = [1]
        wordList.remove(beginWord)
        wordList.add(endWord)
        self.helper([beginWord], wordList, distance, endWord)
        if endWord in wordList:
            return 0
        else:
            return distance[0]
        
    def helper(self, level, wordList, distance, endWord):
        if len(level) == 0:
            return 
        next_level = set()
        for src in level:
            for word in wordList:
                if self.is_valid(word, src):
                    next_level.add(word)
                    if word == endWord:
                        distance[0] += 1
                        wordList.remove(endWord)
                        return
        distance[0] += 1
        wordList -= next_level
        self.helper(list(next_level), wordList, distance, endWord)
                
    
    def is_valid(self, word1, word2):
        count = 0
        for i in xrange(len(word1)):
            if word1[i] != word2[i]:
                count += 1
            if count > 1:
                return False
        return True if count == 1 else False


# method 2, BFS, AC, O(kn)
# similar to method 1, just change the way of finding the words in the wordList that differ only one letter from the current word  
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """
        distance = [1]
        wordList.remove(beginWord)
        wordList.add(endWord)
        self.helper([beginWord], wordList, distance, endWord)
        if endWord in wordList:
            return 0
        else:
            return distance[0]
        
    def helper(self, level, wordList, distance, endWord):
        if len(level) == 0:
            return 
        next_level = []
        distance[0] += 1
        for src in level:
            tmp = [s for s in src]
            for i in xrange(len(tmp)):
                original = tmp[i]
                for j in xrange(26):
                    tmp[i] = chr(97+j)
                    word = ''.join(tmp)
                    if word in wordList:
                        wordList.remove(word)
                        next_level.append(word)
                        if word == endWord:
                            return 
                tmp[i] = original
        self.helper(next_level, wordList, distance, endWord)
                

# method 3, two-end BFS, AC, much faster than method 2 which is  one-end BFS
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """
        head, tail = set(), set()
        head.add(beginWord)
        tail.add(endWord)
        wordList.remove(beginWord)
        wordList.remove(endWord)
        distance = 2
        while len(head)>0 and len(tail)>0:
            if len(head)>len(tail):
                head, tail = tail, head
            next_level = set()
            for word in head:
                tmp = [s for s in word]
                for i in xrange(len(tmp)):
                    letter = tmp[i]
                    for j in xrange(26):
                        tmp[i] = chr(97+j)
                        temp = ''.join(tmp)
                        if temp in tail:
                            return distance
                        if temp in wordList:
                            next_level.add(temp)
                            wordList.remove(temp)
                    tmp[i] = letter
            distance += 1
            head = next_level
        return 0