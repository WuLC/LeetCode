# -*- coding: utf-8 -*-
# Created on Sun Mar 25 2018 11:8:43
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# simple solution
class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        mapping = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        transform = set()
        for word in words:
            transform.add(''.join([mapping[ord(c)-97] for c in word]))
        return len(transform)