# -*- coding: utf-8 -*-
# Created on Mon Apr 30 2018 11:52:39
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# simple solution
class Solution(object):
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        vowel = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        def goat_latin(idx, word):
            if word[0] in vowel:
                word += 'ma'
            else:
                word = word[1:] + word[0] + 'ma'
            word += 'a'*(idx+1)
            return word
        words = S.split()
        new_words = []
        for i in xrange(len(words)):
            new_words.append(goat_latin(i, words[i]))
        return ' '.join(new_words)