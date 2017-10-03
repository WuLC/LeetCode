# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2017-10-03 20:31:20
# @Last Modified by:   WuLC
# @Last Modified time: 2017-10-03 20:32:02
"""

# Employee info
class Employee(object):
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""


# HashMap, recursive
class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        relation = {}
        for e in employees:
            relation[e.id] = (e.importance, e.subordinates)
        return self.helper(relation, id)
            
    
    def helper(self, relation, id):
        if id not in relation:
            return 0
        importance = relation[id][0]
        for sub in relation[id][1]:
            importance += self.helper(relation, sub)
        return importance
        
            