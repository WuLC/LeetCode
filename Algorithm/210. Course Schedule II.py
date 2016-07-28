# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-07-28 14:10:59
# @Last modified by:   WuLC
# @Last Modified time: 2016-07-28 14:11:24
# @Email: liangchaowu5@gmail.com

# topological sort
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        indegree = [0 for i in xrange(numCourses)] 
        connection = {i:[] for i in xrange(numCourses)}
        for link in prerequisites:
            connection[link[1]].append(link[0])
            indegree[link[0]] += 1
        zero_indegree = []
        for i in xrange(numCourses):
            if indegree[i] == 0:
                zero_indegree.append(i)
        i = 0
        while i<len(zero_indegree):
            for node in connection[zero_indegree[i]]:
                indegree[node] -= 1
                if  indegree[node] == 0:
                    zero_indegree.append(node)
            i += 1
        if len(zero_indegree) == numCourses:
            return zero_indegree
        else:
            return []