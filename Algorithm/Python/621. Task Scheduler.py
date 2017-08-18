# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2017-08-19 00:02:56
# @Last Modified by:   LC
# @Last Modified time: 2017-08-19 00:10:14


# simple principle
# refer : https://discuss.leetcode.com/topic/92952/python-straightforward-with-explanation
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        count = [0 for _ in xrange(26)]
        for t in tasks:
            count[ord(t) - 65] += 1
        max_num = max(count)
        m = 0
        for i in xrange(26):
            if count[i] == max_num:
                m += 1
        return max(len(tasks), (max_num - 1) * (n + 1) + m)


# more concise code
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        task_counts = collections.Counter(tasks).values()
        M = max(task_counts)
        Mct = task_counts.count(M)
        return max(len(tasks), (M - 1) * (n + 1) + Mct)
        
        