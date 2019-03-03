# -*- coding: utf-8 -*-
# Created on Sat Mar 02 2019 12:24:51
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# dfs in graph
# with duplicate elements, use counter to record the number of each element
from collections import defaultdict, Counter


class Solution(object):
    def numSquarefulPerms(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        self.count = Counter(A)
        self.result = 0
        self.conn = defaultdict(set)
        for i in xrange(len(A)):
            for j in xrange(i+1, len(A)):
                if A[i]+A[j] == int((A[i]+A[j])**0.5)**2:
                    self.conn[A[i]].add(A[j])
                    self.conn[A[j]].add(A[i])

        for k in self.conn.keys():
            count = defaultdict(int)
            count[k] += 1
            self.dfs(count, k, 1, len(A))
        return self.result

    def dfs(self, count, curr, n, length):
        if n == length:
            self.result += 1
            return
        for num in self.conn[curr]:
            if count[num] < self.count[num]:
                count[num] += 1
                self.dfs(count, num, n+1, length)
                count[num] -= 1

# same idea, another version, more concise code
from collections import Counter
class Solution(object):
    def numSquarefulPerms(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        self.count = Counter(A)
        self.result = 0
        self.conn = {i: {j for j in A if i+j == int((i+j)**0.5)**2} for i in A}
        for k in self.count.keys():
            self.dfs(k, len(A) - 1)
        return self.result

    def dfs(self, curr, left):
        self.count[curr] -= 1
        if left == 0:
            self.result += 1
        for num in self.conn[curr]:
            if self.count[num] > 0:
                self.dfs(num, left-1)
        self.count[curr] += 1