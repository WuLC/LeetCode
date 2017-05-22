# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2017-05-22 09:07:25
# @Last modified by:   WuLC
# @Last Modified time: 2017-05-22 09:07:49
# @Email: liangchaowu5@gmail.com


# hashmap and dfs
class Solution(object):
    
    def __init__(self):
        self.children = {}
        self.killed = []
        
    def killProcess(self, pid, ppid, kill):
        """
        :type pid: List[int]
        :type ppid: List[int]
        :type kill: int
        :rtype: List[int]
        """
        for i in xrange(len(pid)):
            self.children.setdefault(ppid[i], [])
            self.children[ppid[i]].append(pid[i])
        self.kill(kill)
        return self.killed
    
    def kill(self, pid):
        self.killed.append(pid)
        if pid in self.children:
            for id in self.children[pid]:
                self.kill(id)