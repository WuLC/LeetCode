# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2017-03-08 22:46:15
# @Last modified by:   WuLC
# @Last Modified time: 2017-03-08 22:50:17
# @Email: liangchaowu5@gmail.com


# sort the dictionary according to the selecting principle
# then use two pointers to judge whether the word in the dictionary can be form by the given string
class Solution(object):
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        def compare(s1, s2):
            return len(s1) - len(s2) if len(s1)!=len(s2) else cmp(s2,s1)
        def contains(a, b): # judge if b is in a 
            p1, p2 = 0, 0
            while p1 < len(a) and p2 < len(b):
                while p1 < len(a) and b[p2] != a[p1]:
                    p1 +=1
                if p1 == len(a):
                    return False
                else:
                     p1 += 1
                     p2 += 1
            return True if p2 == len(b) else False
            
            
        d.sort(cmp = compare)
        for i in reversed(xrange(len(d))):
            if contains(s, d[i]):
                return d[i]
        return ''
    
            