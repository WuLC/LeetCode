# -*- coding: utf-8 -*-
# Created on Wed Apr 10 2019 22:16:11
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# two pointers
class Solution(object):
    def camelMatch(self, queries, pattern):
        """
        :type queries: List[str]
        :type pattern: str
        :rtype: List[bool]
        """
        return [self.match(query, pattern) for query in queries]
    
    def match(self, query, pattern):
        p1, p2 = 0, 0
        n1, n2 = len(query), len(pattern)
        while p1 < n1 and p2 <= n2:
            if p2 == n2:
                while p1 < n1:
                    if query[p1].isupper():
                        return False
                    p1 += 1
            else:
                while p1 < n1 and query[p1] != pattern[p2]:
                    if query[p1].isupper():
                        return False
                    p1 += 1
                p1 += 1
                p2 += 1
        return p1 == n1 and p2 == n2
