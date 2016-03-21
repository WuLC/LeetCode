#encoding:utf-8
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        matchDict = {'(':')','[':']','{':'}'}
        stack = []
        index = -1
        for i in range(len(s)):
            if s[i] == '(' or s[i]=='[' or s[i]=='{':
                stack.append(s[i])
                index += 1
            else:
                if len(stack)==0:
                    return False  #防止只有右括号，stack为空
                if not matchDict[stack.pop(index)] == s[i]: 
                    return False
                index -= 1
                
        if len(stack) == 0:
            return True
        else: 
            return False