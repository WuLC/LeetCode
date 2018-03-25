# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2016-01-30 22:38:53
# @Last modified by:   LC
# @Last Modified time: 2016-04-10 16:23:53
# @Email: liangchaowu5@gmail.com
 
# dp, O(n^2)
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        dp = [[False for j in xrange(n)] for i in xrange(n)]
        result = ''
        for i in reversed(xrange(n)):
            for j in xrange(i, n):
                if i == j:
                    dp[i][j] = True
                elif s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] if i+1<=j-1 else True
                if dp[i][j] and j-i+1 > len(result):
                    result = s[i:j+1]
        return result   
    
    
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


            
                
                        
                
            