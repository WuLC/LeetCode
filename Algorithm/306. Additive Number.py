# -*- coding: utf-8 -*-
# @Author: WuLC 
# @Date:   2016-08-15 00:01:33
# @Last modified by:   WuLC
# @Last Modified time: 2016-08-15 00:10:18
# @Email: liangchaowu5@gmail.com


# method 1, solution with an index
class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        n = len(num)
        for i in xrange(n/2):
            for j in xrange(i+1, i+1+(n-i-1)/2):
                n1, n2 = num[:i+1], num[i+1:j+1]
                if self.helper(n1, n2, j+1, num):
                    return True
        return False
     
    def helper(self, n1, n2, idx, num):
        if (len(n1) > 1 and n1[0] == '0') or (len(n2) > 1 and n2[0] == '0'):
            return False
        total = self.add(n1, n2)
        if total == num[idx:]:
            return True
        elif len(total) > len(num)-idx or total != num[idx:idx+len(total)]:
            return False
        else:
            return self.helper(n2, total, idx+len(total), num)

            
    def add(self, n1, n2):
        i,j = len(n1)-1, len(n2)-1
        result, carry = [], 0
        while i>=0 or j>=0:
            tmp = carry
            if i>=0: tmp += int(n1[i])
            if j>=0: tmp += int(n2[j])
            result.append(str(tmp%10))
            carry = tmp/10
            i -= 1
            j -= 1
        if carry:
            result.append('1')
        result.reverse()
        return ''.join(result)
    

# method 2, solution without an index
class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        n = len(num)
        for i in xrange(n/2):
            for j in xrange(i+1, i+1+(n-i-1)/2):
                n1, n2 = num[:i+1], num[i+1:j+1]
                if self.helper(n1, n2, num[j+1:]):
                    return True
        return False
     
    def helper(self, n1, n2, num):
        if (len(n1) > 1 and n1[0] == '0') or (len(n2) > 1 and n2[0] == '0'):
            return False
        total = self.add(n1, n2)
        if total == num:
            return True
        elif len(total) >= len(num) or total != num[:len(total)]:
            return False
        else:
            return self.helper(n2, total, num[len(total):])
            
    def add(self, n1, n2):
        i,j = len(n1)-1, len(n2)-1
        result, carry = [], 0
        while i>=0 or j>=0:
            tmp = carry
            if i>=0: tmp += int(n1[i])
            if j>=0: tmp += int(n2[j])
            result.append(str(tmp%10))
            carry = tmp/10
            i -= 1
            j -= 1
        if carry:
            result.append('1')
        result.reverse()
        return ''.join(result)