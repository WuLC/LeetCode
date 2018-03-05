# -*- coding: utf-8 -*-
# Created on Sat Feb 17 2018 9:41:7
# Author: WuLC
# EMail: liangchaowu5@gmail.com


# priority queue, time O(nlogk), space O(n)
# define custom compare function with Element class

import collections
import heapq

class Element:
    def __init__(self, word, count):
        self.count = count
        self.word = word
        
    def __lt__(self, other):
        if self.count == other.count:
            return self.word > other.word
        return self.count < other.count
    
class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        counts = collections.Counter(words)
        freqs = []
        for word, count in counts.items():
            heapq.heappush(freqs, Element(word, count))
            if len(freqs) > k:
                heapq.heappop(freqs)
        
        return [heapq.heappop(freqs).word for _ in xrange(len(freqs))][::-1]