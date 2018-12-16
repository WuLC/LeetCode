# -*- coding: utf-8 -*-
# Created on Sun Dec 16 2018 10:54:0
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# hashtable
# there is always a loop, but how to prove
class Solution(object):
    def prisonAfterNDays(self, cells, N):
        """
        :type cells: List[int]
        :type N: int
        :rtype: List[int]
        """
        p1, p2 = cells, [0] * len(cells)
        record, reversed_record = {}, {}
        for i in xrange(N):
            num = reduce(lambda x, y: str(x)+str(y), p1)
            if num in record:
                left = (N - record[num]) % (i - record[num])
                return [int(c) for c in reversed_record[record[num] + left]]
            else:
                record[num] =  i
                reversed_record[i] = num
            for j in xrange(1, len(cells) - 1):
                p2[j] = 1 if p1[j-1] == p1[j+1] else 0
            p1, p2 = p2, p1
            p2[0], p2[-1] = 0, 0
        return p1