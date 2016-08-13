# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-08-13 09:49:43
# @Last modified by:   WuLC
# @Last Modified time: 2016-08-13 09:49:55
# @Email: liangchaowu5@gmail.com

class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums, self.pos = [], {}

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.pos:
            self.nums.append(val)
            self.pos[val] = len(self.nums)-1
            return True
        return False
        
    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.pos:
            idx = self.pos[val]
            self.pos[self.nums[-1]] = idx
            self.nums[idx]  = self.nums[-1]
            self.nums.pop()
            del self.pos[val]
            return True
        return False
        

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return self.nums[random.randint(0, len(self.nums)-1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()