# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2017-07-09 11:00:19
# @Last Modified by:   WuLC
# @Last Modified time: 2017-07-09 15:13:30


# recursive methods have various problems
# dp with constant lead to TLE

# recursive
# slicing lead to MLE
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if (len(s)) == 0:
            return 1
        elif len(s) == 1:
            if s == '0':
                return 0
            elif s == '*':
                return 9
            else:
                return 1
        else:
            if s[0] == '0':
                return 0
            count = 0
            
            # one char prefix
            pre = 9 if s[0] == '*' else 1
            left = self.numDecodings(s[1:])
            count += pre * left
            
            # two char prefix
            if s[0] == '*' and s[1] == '*':
                pre = 15
            elif s[0] == '*':
                pre = 1 if int(s[1]) > 6 else 2
            elif s[1] == '*':
                if int(s[0]) > 2:
                    pre = 0
                elif int(s[0]) == 2:
                    pre = 6
                elif int(s[0]) == 1:
                    pre = 9
            else:
                pre = 1 if int(s[:2]) <= 26 else 0
            left = self.numDecodings(s[2:])
            count += pre * left
        return count % 1000000007

# recursive
# with index: maximum recursion depth exceeded in cmp
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        return self.helper(0, s)

    def helper(self, i, s):
        if i == len(s):
            return 1
        elif len(s) - i == 1:
            if s[i] == '0':
                return 0
            elif s[i] == '*':
                return 9
            else:
                return 1
        else:
            if s[i] == '0':
                return 0
            count = 0
            
            # one char prefix
            pre = 9 if s[i] == '*' else 1
            left = self.helper(i+1, s)
            count += pre * left
            
            # two char prefix
            if s[i] == '*' and s[i + 1] == '*':
                pre = 15
            elif s[i] == '*':
                pre = 1 if int(s[i+1]) > 6 else 2
            elif s[i+1] == '*':
                if int(s[i]) > 2:
                    pre = 0
                elif int(s[i]) == 2:
                    pre = 6
                elif int(s[i]) == 1:
                    pre = 9
            else:
                pre = 1 if int(s[i:i+2]) <= 26 else 0
            left = self.helper(i+2, s)
            count += pre * left
        return count % 1000000007
            
                
# dp with constant space, TLE
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        def parseOne(s):
            if s == '*':
                return 9
            return 0 if s == '0' else 1
        
        def parseTwo(s):
            if s[0] == '0':
                return 0
            elif s[0] == '*' and s[1] == '*':
                return 15
            elif s[0] == '*':
                return 1 if int(s[1]) > 6 else 2
            elif s[1] == '*':
                if int(s[0]) > 2:
                    return 0
                elif int(s[0]) == 1:
                    return 9
                elif int(s[0]) == 2:
                    return 6
            else:
                return 1 if int(s) <= 26 else 0
        
        pre1 = 1
        pre2 = parseOne(s[0])
        curr = pre2
        for i in xrange(1, len(s)):
            curr = (pre2 * parseOne(s[i]) + pre1 * parseTwo(s[i-1]+s[i])) % 1000000007
            pre1 = pre2
            pre2 = curr
        return curr 


                
        