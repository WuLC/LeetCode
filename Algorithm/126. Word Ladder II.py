# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-08-07 21:10:52
# @Last modified by:   WuLC
# @Last Modified time: 2016-08-17 10:05:12
# @Email: liangchaowu5@gmail.com

# method 1, one end BFS, find all the results and chooses the min_length from it , TLE
class Solution(object):
    def findLadders(self, beginWord, endWord, wordlist):
        """
        :type beginWord: str
        :type endWord: str
        :type wordlist: Set[str]
        :rtype: List[List[int]]
        """
        result, link = [], []
        wordlist.add(endWord)
        self.helper(beginWord, wordlist, [beginWord], endWord, result)
        if len(result) == 0:
            return result
        min_length = min(map(lambda x:len(x), result))
        return [result[i] for i in xrange(len(result)) if len(result[i])==min_length]
        
    def helper(self, src, wordlist, words, endWord, result):
        wordlist.remove(src)
        tmp = [s for s in src]
        for i in xrange(len(tmp)):
            original = tmp[i]
            for j in xrange(26):
                tmp[i] = chr(97+j)
                word = ''.join(tmp)
                if word in wordlist:
                    words.append(word)
                    if word == endWord:
                        result.append(words[:])
                        words.pop()
                        wordlist.add(src)  
                        return 
                    self.helper(word, wordlist, words, endWord, result)  
                    words.pop()
            tmp[i] = original
        wordlist.add(src)

# method 2, one end BFS, TLE
class Solution(object):
    def findLadders(self, beginWord, endWord, wordlist):
        """
        :type beginWord: str
        :type endWord: str
        :type wordlist: Set[str]
        :rtype: List[List[int]]
        """
        result, link = [], []
        wordlist.add(endWord)
        self.helper([beginWord], wordlist, [], endWord, result)
        return result
        
        
    def helper(self, level, wordlist, words, endWord, result):
        wordlist -= set(level)
        for src in level:
            flag = 0
            next_level = []
            tmp = [s for s in src]
            for i in xrange(len(tmp)):
                original = tmp[i]
                for j in xrange(26):
                    tmp[i] = chr(97+j)
                    word = ''.join(tmp)
                    if word in wordlist:
                        next_level.append(word)
                        if word == endWord:
                            flag = 1
                            words.append(src)
                            words.append(word)
                            result.append(words[:])
                            words.pop()
                            words.pop()
                            break 
                tmp[i] = original
                if flag == 1: break
            if len(next_level)>0 and flag == 0:
                words.append(src)
                self.helper(next_level, wordlist, words, endWord, result)
                words.pop()
        #wordlist = wordlist.union(set(level)) # rebinding mutable variable can not change the variabe in a function
        for w in set(level): wordlist.add(w)  


# method 3, BFS then DFS, AC
# BFS to find all possible connections, DFS to find the valid connection from the result botained by BFS
class Solution(object):
    def findLadders(self, beginWord, endWord, wordlist):
        """
        :type beginWord: str
        :type endWord: str
        :type wordlist: Set[str]
        :rtype: List[List[int]]
        """
        head, result, link = set(), [], [] # element for link-[{word:[]}]
        head.add(beginWord)
        found = False
        while len(head)>0:
            next_level = set()
            tmp_link = {}
            wordlist -= head
            for word in head:
                tmp = [s for s in word]
                for i in xrange(len(tmp)):
                    letter = tmp[i]
                    for j in xrange(26):
                        tmp[i] = chr(97+j)
                        temp = ''.join(tmp)
                        if temp == endWord:
                            found = True
                        if temp in wordlist and temp not in tmp_link:
                            next_level.add(temp)
                            tmp_link.setdefault(word, [])
                            tmp_link[word].append(temp)
                    tmp[i] = letter
            link.append(tmp_link)
            if found:
                break
            head = next_level
        if found:
            self.dfs(link , beginWord, endWord, 0, [beginWord], result)
        return result

    def dfs(self, link ,word, ew, idx, tmp, result):
        if idx == len(link)-1:
            if ew in link[idx][word]:
                tmp.append(ew)
                result.append(tmp[:])
                tmp.pop()
            return 
        else:
            for w in link[idx][word]:
                if w in link[idx+1]:
                    tmp.append(w)
                    self.dfs(link, w, ew, idx+1, tmp, result)
                    tmp.pop()
        
        