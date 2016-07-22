# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2016-07-22 21:45:20
# @Last modified by:   WuLC
# @Last Modified time: 2016-07-22 22:09:36
# @Email: liangchaowu5@gmail.com

# method 1, complicated judge 
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.replace(' ','')
        nums, ope = [], []
        operator = ['+', '-', '*', '/']
        idx = 0
        while idx < len(s):
            if s[idx] in operator:
                if len(ope) > 0 and ope[-1] in ['*', '/']:
                    if ope.pop() == '*':
                        tmp = nums.pop() * nums.pop()
                    else:
                        n1 = nums.pop()
                        n2 = nums.pop()
                        tmp = n2 / n1
                    nums.append(tmp)
                ope.append(s[idx])
                idx += 1
            else:
                nu = ''
                while idx < len(s) and s[idx] not in operator: # number more than one bit
                    nu += s[idx]
                    idx += 1
                nums.append(int(nu))

        if len(ope) > 0 and ope[-1] in ['*', '/']:
            if ope.pop() == '*':
                tmp = nums.pop() * nums.pop()
            else:
                n1 = nums.pop()
                n2 = nums.pop()
                tmp = n2 / n1
            nums.append(tmp)
    
        for i in xrange(len(ope)):
            if ope[i] == '+':
                nums[i+1] = nums[i] + nums[i+1]
            elif ope[i] == '-':
                nums[i+1] = nums[i] - nums[i+1]
        return nums[-1]


# method, find next integer each time
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.replace(' ','')
        nums, ope = [], []
        operator = ['+', '-', '*', '/']
        idx = 0
        while idx < len(s):
            if s[idx] in operator:
                if s[idx] == '*':
                    next_int, idx = self.find_next(s, idx+1)
                    tmp = nums.pop() * next_int
                    nums.append(tmp)
                elif s[idx] == '/':
                    next_int, idx = self.find_next(s, idx+1)
                    tmp = nums.pop() / next_int
                    nums.append(tmp)
                else:
                    ope.append(s[idx])
                    idx += 1
            else:
                next_int, idx = self.find_next(s, idx)
                nums.append(next_int)
            
        for i in xrange(len(ope)):
            if ope[i] == '+':
                nums[i+1] = nums[i] + nums[i+1]
            elif ope[i] == '-':
                nums[i+1] = nums[i] - nums[i+1]
        return nums[-1]
        
    def find_next(self, s, idx):
        operator = ['+', '-', '*', '/']
        nu = ''
        while idx < len(s) and s[idx] not in operator:
            nu += s[idx]
            idx += 1
        next_int = int(nu)
        return (next_int, idx)