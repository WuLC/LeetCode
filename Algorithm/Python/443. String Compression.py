# -*- coding: utf-8 -*-
# Created on Sun Oct 29 2017 11:16:56
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# extract the compressed string
class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        compressedString = ''
        char, count = chars[0], 1
        for i in xrange(1, len(chars)):
            if chars[i] != char:
                compressedString += char
                if count > 1:
                    compressedString += str(count)
                count = 1
            else:
                count += 1
            char = chars[i]
        compressedString += char
        if count > 1:
            compressedString += str(count)
        original, compressed = len(chars), len(compressedString)
        if original >= compressed:
            for i in xrange(compressed):
                chars[i] = compressedString[i]
            return compressed
        else:
            return original
        