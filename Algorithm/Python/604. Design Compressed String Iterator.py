# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2017-06-11 12:00:07
# @Last modified by:   LC
# @Last Modified time: 2017-06-11 12:01:00
# @Email: liangchaowu5@gmail.com

# seperate letters from numbers
class StringIterator(object):

    def __init__(self, compressedString):
        """
        :type compressedString: str
        """
        self.letters = []
        self.nums = []
        idx = 0
        while idx < len(compressedString):
            if compressedString[idx].isalpha():
                self.letters.append(compressedString[idx])
                idx += 1
            else:
                tmp = ''
                while idx < len(compressedString) and compressedString[idx].isdigit():
                    tmp += compressedString[idx]
                    idx += 1
                self.nums.append(int(tmp))
        self.idx = -1
        self.count = 0
        

    def next(self):
        """
        :rtype: str
        """
        if self.count == 0:
            self.idx += 1
            if self.idx >= len(self.letters):
                return ' '
            self.count = self.nums[self.idx]
        self.count -= 1
        return self.letters[self.idx]
        

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.count == 0:
            self.idx += 1
            if self.idx >= len(self.letters):
                return False
            self.count = self.nums[self.idx]
        return True
        
        


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()