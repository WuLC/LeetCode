# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-07-28 11:48:49
# @Last modified by:   WuLC
# @Last Modified time: 2016-07-28 14:08:40
# @Email: liangchaowu5@gmail.com

# pure DFS, TLE
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        course = [[0 for i in xrange(numCourses)] for j in xrange(numCourses)]
        for s in prerequisites:
            course[s[0]][s[1]] = 1
            
        visited = set()
        for i in xrange(numCourses):
            if self.dfs(course, i, visited)==False:
                return False
        return True
                
        
    def dfs(self, course, num, visited):
        for i in xrange(len(course[num])):
            if course[num][i] == 1:
                visited.add(num)
                if i in visited:
                    return False
                else:
                    if self.dfs(course, i, visited) == False:
                        return False
                    visited.remove(num)
                    
        
# Topological Sort
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
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
            return True
        else:
            return False