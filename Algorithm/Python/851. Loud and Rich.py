# -*- coding: utf-8 -*-
# Created on Sun Jun 10 2018 18:6:39
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# simple dfs, TLE
from collections import defaultdict
class Solution(object):
    def loudAndRich(self, richer, quiet):
        """
        :type richer: List[List[int]]
        :type quiet: List[int]
        :rtype: List[int]
        """
        record = defaultdict(list)
        for x, y in richer:
            record[y].append(x)
        result = []
        for i in xrange(len(quiet)):
            result.append(self.helper(record, i, quiet))
        return result
    
    def helper(self, record, idx, quiet):
        """return index of person that is richer than idx and is the least quiet"""
        if idx not in record:
            return idx
        r = idx
        for i in xrange(len(record[idx])):
            tmp = self.helper(record, record[idx][i], quiet)
            if quiet[r] > quiet[tmp]:
                r = tmp
        return r
        
# dfs with cache, AC
from collections import defaultdict
class Solution(object):
    def loudAndRich(self, richer, quiet):
        """
        :type richer: List[List[int]]
        :type quiet: List[int]
        :rtype: List[int]
        """
        self.cache = {}
        record = defaultdict(list)
        for x, y in richer:
            record[y].append(x)
        result = []
        for i in xrange(len(quiet)):
            result.append(self.helper(record, i, quiet))
        return result
    
    def helper(self, record, idx, quiet):
        """return index of person that is richer than idx and is the least quiet"""
        if idx not in record:
            return idx
        if idx not in self.cache:  
            r = idx
            for i in xrange(len(record[idx])):
                tmp = self.helper(record, record[idx][i], quiet)
                if quiet[r] > quiet[tmp]:
                    r = tmp
            self.cache[idx] = r
        return self.cache[idx]