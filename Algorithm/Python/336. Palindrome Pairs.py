# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-09-28 22:46:52
# @Last modified by:   WuLC
# @Last Modified time: 2016-09-28 23:00:41
# @Email: liangchaowu5@gmail.com

# Trie, HashTable
class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        result = []
        # build Trie
        root = {}
        for i in xrange(len(words)):
            curr = root
            for char in words[i][::-1]:
                curr.setdefault(char, {})
                curr = curr[char]
            curr['#'] = i # represents a word
        
        # search
        for i in xrange(len(words)):
            # ignore empty string, cause the following code has dealt with it
            if len(words[i]) == 0:
                continue

    
            curr, match = root, True
            for j in xrange(len(words[i])):
                if '#' in curr and  self.is_palindrome(words[i][j:]) and curr['#'] != i:
                    result.append([i, curr['#']])
                    if curr == root: # empty string matches from both sides
                        result.append([curr['#'], i])
                if words[i][j] in curr:
                    curr = curr[words[i][j]]
                else:
                    match = False
                    break
            if match:
                for index in self.dfs(curr, ''):
                    if index != i:
                        result.append([i,index])
        return result
                
    # find all the palindrome string under root and return its' indices
    def dfs(self, root, tmp):
        if len(root) == 1 and '#' in root:
            return [root['#']] if self.is_palindrome(tmp) else []
        indices = []
        if '#' in root and self.is_palindrome(tmp):
            indices.append(root['#'])
        for k,v in root.items():
            if k != '#':
                indices += self.dfs(v, tmp+k)
        return indices
            
    def is_palindrome(self, s):
        i, j = 0, len(s) - 1 
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True