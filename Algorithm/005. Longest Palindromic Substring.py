#encoding:utf-8
################################################
#方法一：从长到短遍历字符串，判断每次得到的子字符串是否为回文字符串，时间复杂度为O(n^3)
#将判断一个字符串是否为回文字符串封装成函数isPalindromic，但是leetcode提示找不到这个函数
################################################
class Solution(object):
    def isPalindromic(self,s):
        strLen=len(s)
        flag=True
        mid=0
        if strLen%2==0:
            mid=strLen/2
        else:
            mid=(strLen-1)/2
            
        for i in range(mid):
            if s[i] != s[strLen-1-i]:
                flag=False
                break
        return flag
        
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        strLen=len(s)
        for i in range(strLen): #the number of characters cut down each time 
            for j in range(i+1):
                subStr=s[j:strLen-i+1]
                if self.isPalindromic(subStr):
                    return subStr
    
    
#################################################
#方法二：从中间字母向两边展开比较，时间复杂度为O(n^2)
##################################################
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        r=s[0]
        if len(s) > 1:
            for i in range (1,len(s)):
                #oddResult
                begin=i 
                end=i
                oddResult=self.getPalindoreStr(s,begin,end)
                if oddResult != None and len(oddResult)> len(r):
                    r=oddResult

                #enevResult
                begin=i-1
                end=i
                evenResult=self.getPalindoreStr(s,begin,end)
                if evenResult != None and len(evenResult)> len(r):
                    r=evenResult
        return r

    #从给定的begin和end位置先两边扩展，得到回文字符串                
    def getPalindoreStr(self,s,begin,end):
        while ( begin>=0 and end<len(s) and s[begin]==s[end] ):
                begin-=1
                end+=1
        result=s[begin+1:end] if  begin+1 <= end else None
        return result


            
                
                        
                
            