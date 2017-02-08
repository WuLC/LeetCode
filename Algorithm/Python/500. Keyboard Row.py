# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2017-02-08 15:35:27
# @Last modified by:   WuLC
# @Last Modified time: 2017-02-08 15:36:28
# @Email: liangchaowu5@gmail.com

# hashmap
class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        rows = {'qwertyuiop':1, 'asdfghjkl':2, 'zxcvbnm':3}
        charMap = {}
        for s, row in rows.items():
            for char in s:
                charMap[char] = row
        result = []
        for word in words:
            if len(word) == 0:
                continue
            row = charMap[word[0].lower()]
            if all([charMap[c.lower()] == row for c in word]):
                result.append(word)
        return result