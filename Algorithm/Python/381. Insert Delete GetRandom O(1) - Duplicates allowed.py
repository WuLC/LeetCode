# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-08-13 09:51:05
# @Last modified by:   WuLC
# @Last Modified time: 2016-08-13 09:51:18
# @Email: liangchaowu5@gmail.com

class RandomizedCollection(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums, self.pos = [], {}

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        self.nums.append(val)
        if val not in self.pos:
            self.pos[val] = [len(self.nums)-1]
            return True
        else:
            self.pos[val].append(len(self.nums)-1)
            return False
        
    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.pos:
            if val == self.nums[-1]:
                self.pos[val].pop()
                self.nums.pop()
            else:
                idx = self.pos[val].pop()
                self.pos[self.nums[-1]].pop()
                #self.pos[self.nums[-1]].append(idx)
                indices = self.pos[self.nums[-1]]
                i = 0
                for i in xrange(len(indices)):
                    if idx < indices[i]:
                        indices.insert(i, idx)
                        break
                if i == len(indices):
                    indices.append(idx)
                self.nums[idx] = self.nums[-1]
                self.nums.pop()
            if len(self.pos[val]) == 0:
                del self.pos[val]
            return True
        return False
        

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        return self.nums[random.randint(0, len(self.nums)-1)]
        

# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()