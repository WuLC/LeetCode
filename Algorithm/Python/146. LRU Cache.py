# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-08-04 22:39:03
# @Last modified by:   WuLC
# @Last Modified time: 2016-08-04 22:40:49
# @Email: liangchaowu5@gmail.com

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = {}
        self.keys = collections.deque()
        self.exist_keys = set()
        
        
    def get(self, key):
        """
        :rtype: int
        """
        if key in self.exist_keys:
            self.keys.remove(key)
            self.keys.append(key)
            return self.cache[key]
        return -1
        

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        if key not in self.exist_keys:
            self.exist_keys.add(key)
            if len(self.keys) == self.capacity:
                # remove the LRU element
                old_key = self.keys.popleft()
                self.exist_keys.remove(old_key)
                del self.cache[old_key]
        else:
            self.keys.remove(key)
        self.keys.append(key)
        self.cache[key] = value
            
                
                
        