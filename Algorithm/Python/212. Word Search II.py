# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-11-23 15:27:48
# @Last modified by:   WuLC
# @Last Modified time: 2016-11-23 15:37:22
# @Email: liangchaowu5@gmail.com





# Trie and dfs 
# referer: https://discuss.leetcode.com/topic/33246/java-15ms-easiest-solution-100-00
# still TLE
class TrieNode:
    def __init__(self):
        self.next = [None for i in xrange(26)]
        self.word = None

class Solution(object):
    def __init__(self):
        self.result = None 
        self.m = None
        self.n = None
        
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        if len(board) == 0 or len(board[0])==0:
            return []
        root = TrieNode()
        self.result = []
        
        # build Trie
        for word in words:
            curr = root
            for char in word:
                idx = ord(char)-97
                if curr.next[idx] == None:
                    curr.next[idx] = TrieNode()
                curr = curr.next[idx]
            curr.word = word
        
        # search on the board
        self.m, self.n = len(board), len(board[0])
        for i in xrange(self.m):
            for j in xrange(self.n):
                self.dfs(board, i, j, root)
        return self.result
    
    def dfs(self, board, i, j, curr_node):
        tmp =  board[i][j]
        if tmp == '#' or curr_node.next[ord(tmp) - 97] == None:
            return
        board[i][j] = '#'
        curr_node = curr_node.next[ord(tmp) - 97]
        if curr_node.word != None:
            self.result.append(curr_node.word)
            curr_node.word = None  # cannot return immedially as there may still exist longer word
        moves = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        for move in moves:
            if 0 <= i+move[0] < self.m and 0 <= j+move[1] < self.n:
                self.dfs(board, i+move[0], j+ move[1], curr_node)
        board[i][j] = tmp 