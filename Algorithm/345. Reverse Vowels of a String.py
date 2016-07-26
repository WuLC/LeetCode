# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-07-26 12:59:04
# @Last modified by:   WuLC
# @Last Modified time: 2016-07-26 12:59:21
# @Email: liangchaowu5@gmail.com

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = [ 'a', 'e', 'i', 'o', 'u']
        indices, chars = [], []
        for i in xrange(len(s)):
            chars.append(s[i])
            if s[i].lower() in vowels:
                indices.append(i)
        left, right = 0, len(indices)-1
        while left < right:
            p, q = indices[left], indices[right]
            chars[p], chars[q] = chars[q], chars[p]
            left += 1
            right -= 1
        return ''.join(chars)