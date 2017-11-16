# -*- coding: utf-8 -*-
# Created on Fri Nov 17 2017 0:17:52
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# regular expression, hashtable, stack
# base on the solution: https://discuss.leetcode.com/topic/110534/neat-python-with-explanation-35ms
import re
from collections import defaultdict
class Solution(object):
    def countOfAtoms(self, formula):
        """
        :type formula: str
        :rtype: str
        """
        stack = []
        tokens = list(filter(lambda c: c, re.split('([A-Z]{1}[a-z]?|\(|\)|\d+)', formula)))
        count = defaultdict(int)
        i = 0
        while i < len(tokens):
            token = tokens[i]
            if token == '(':
                stack.append(count)
                stack.append(token)
                count = defaultdict(int)
            elif token == ')':
                tmp = stack.pop()
                while tmp != '(':
                    for k,v in tmp.items():
                        count[k] += v
                    tmp = stack.pop()
            elif token.isdigit():
                if tokens[i-1] == ')':
                    for k, v in count.items():
                        count[k] = v * int(token)
                else:
                    count[tokens[i-1]] += int(token) - 1
            else:
                count[token] += 1
            i += 1
        while stack:
            tmp = stack.pop()
            for k,v in tmp.items():
                count[k] += v
        sorted_count = sorted(count.items(), key=lambda (k,v):k)
        result = ''
        for k, v in sorted_count:
            result += k
            if v != 1:
                result += str(v)
        return result