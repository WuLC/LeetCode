# -*- coding: utf-8 -*-
# Created on Tue Dec 12 2017 16:44:38
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# naive solution
class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        larger, smallest = None, None
        for letter in letters:
            if letter > target:
                larger = letter if larger == None else min(larger, letter)
            smallest = letter if smallest == None else min(smallest, letter)
        return larger if larger else smallest