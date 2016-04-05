# 方法一，超时，时间复杂度O(n^2)
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s)<2:
           return 0
        left = 0
        right = 0
        for i in range(len(s)):
            if s[i] == '(':
                left+=1
            elif s[i] == ')':
                right+=1
        
        m = min(left,right)
        
        cut = len(s)-2*m # 从长到短遍历
        while cut<=len(s)-2:
            subLen = len(s) - cut
            for i in range(cut+1):
                subStr = s[i:i+subLen]
                if subStr[0] == ')':
                    continue
                if self.isValid(subStr):
                    return subLen
            cut +=2        
            
    def isValid(self,s):
        stack = []
        for i in range(len(s)):
            if s[i] == '(':
                stack.append('(')
            elif s[i] == ')':
                if len(stack)>0:
                    stack.pop(len(stack)-1)
                else:
                    break
            
        if len(stack)==0 and i==len(s)-1:
            return True
        else:
            return False
            
                
            

# 方法二，动态规划，时间复杂度O(n)，能够AC
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        longest = []
        longest.append(0)
        for i in range(1,len(s)):
            if s[i] == '(':
                longest.append(0)
            else:
                if i-1>=0 and s[i-1]=='(':
                    longest.append(longest[i-2]+2)
                elif i-1>=0 and s[i-1]==')' and i-longest[i-1]-1 >=0 and s[i-longest[i-1]-1]=='(':
                    tmp = longest[i-longest[i-1]-2] if i-longest[i-1]-2>=0 else 0
                    longest.append(longest[i-1]+2+tmp)
                else:
                    longest.append(0)
        return max(longest)
                    
