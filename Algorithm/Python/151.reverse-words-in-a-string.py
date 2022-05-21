#
# @lc app=leetcode id=151 lang=python
#
# [151] Reverse Words in a String
#

# @lc code=start
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # strip leading and tailing spaces
        start, end = 0, len(s) - 1
        while s[start] == " ":
            start += 1
        while s[end] == " ":
            end -= 1
        chars = [c for c in s[start:end+1]]

        # reverse the whole string
        self.reverse(chars, 0, len(chars) - 1)
        
        # reverse word by word
        p1, p2 = 0, 0
        while p2 <= len(chars):
            if p2 == len(chars) or chars[p2] == ' ':
                self.reverse(chars, p1, p2-1)
                while p2 < len(chars) and chars[p2] == ' ': # multiple spaces
                    p2 += 1
                p1 = p2
            p2 += 1
        
        # concate final string
        result = ""
        for c in chars:
            if c == ' ' and result[-1] == ' ':
                continue
            result += c
        return result

    def reverse(self, chars, start, end):
        while start < end:
            tmp = chars[start]
            chars[start] = chars[end]
            chars[end] = tmp
            start += 1
            end -= 1
        
# @lc code=end

