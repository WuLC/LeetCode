# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2016-07-24 20:31:48
# @Last modified by:   WuLC
# @Last Modified time: 2016-07-24 21:38:09
# @Email: liangchaowu5@gmail.com

# method 1, recursively, TLE
class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        nodes = preorder.split(',')
        return self.helper(nodes)
        
    def helper(self, nodes):
        if len(nodes) == 0:
            return True
        elif len(nodes) % 2 == 0:
            return False
            
        if nodes[0] == '#':
            if len(nodes) > 1:
                return False
            else:
                return True
        for i in xrange(1,len(nodes), 2):
            if self.helper(nodes[1:i+1]) and self.helper(nodes[i+1:]):
                return True
        return False


# method 2, consider indegree and outdegree
class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        nodes = preorder.split(',')
        indegree, outdegree = 0, 1
        for i in xrange(len(nodes)):
            indegree += 1
            if outdegree - indegree < 0:
                return False
            if nodes[i] != '#':
                outdegree += 2
        return (indegree - outdegree)==0