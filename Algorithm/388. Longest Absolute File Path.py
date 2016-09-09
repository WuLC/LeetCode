# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2016-09-09 09:34:38
# @Last modified by:   WuLC
# @Last Modified time: 2016-09-09 11:30:01
# @Email: liangchaowu5@gmail.com


# using stack
# split with '\n',when meeting a line with number of '\t' no larger than the element on the top of the stack
# pop until, the stack is empty or the top element has less '\t' than the current line
# O(n) time, O(n) space
class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        lines = input.split('\n')
        words, tab_count = [], []
        result = 0
        for i in xrange(len(lines)):
            count = self.tab_count(lines[i])
            word = lines[i][count:]
            while tab_count and count <= tab_count[-1]:
                tab_count.pop()
                words.pop()
            if '.' in word:
                words.append(word)
                result = max(result, len('/'.join(words)))
                words.pop()
            else:
                words.append(lines[i][count:])
                tab_count.append(count)
        return result

   
    def tab_count(self, s):
        index, count = 0, 0
        while index < len(s):
            
            if s[index] == '\t':
                count += 1
                index += 1
            else:
                return count



# based on the above solution, change the method of counting '\t'
class Solution(object):
    def lengthLongestPath(self, input):
        lines = input.split('\n')
        words, tab_count = [], []
        result = 0
        for i in xrange(len(lines)):
            word = lines[i].lstrip('\t')
            count = len(lines[i]) - len(word)
            while tab_count and count <= tab_count[-1]:
                tab_count.pop()
                words.pop()
            if '.' in word:
                words.append(word)
                result = max(result, len('/'.join(words)))
                words.pop()
            else:
                words.append(word)
                tab_count.append(count)
        return result


# another solution
# store the length of each level in a dictionary
class Solution(object):
    def lengthLongestPath(self, input):
        maxlen = 0
        pathlen = {0: 0}
        for line in input.splitlines():
            name = line.lstrip('\t')
            depth = len(line) - len(name)
            if '.' in name:
                maxlen = max(maxlen, pathlen[depth] + len(name))
            else:
                pathlen[depth + 1] = pathlen[depth] + len(name) + 1
        return maxlen