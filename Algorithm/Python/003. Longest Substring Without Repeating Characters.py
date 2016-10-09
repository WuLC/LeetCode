# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2016-01-24 11:02:34
# @Last modified by:   LC
# @Last Modified time: 2016-04-10 16:23:30
# @Email: liangchaowu5@gmail.com


#########################################
#方法一：遍历以每个字符开头的最长子串
#时间复杂度：O(n^2)
#结果：最后一项超时
########################################
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max=0
        for  i in range(len(s)):
           tmp=[]
           tmp.append(s[i])
           for j in range(i+1,len(s)):
               if s[j] not in tmp:
                   tmp.append(s[j])
               else:
                   if len(tmp)>max:
                       max=len(tmp)
                       break
        return max
                
        
##############################################
#方法二：不遍历每个字符作为开头，而是以与当前字符重复的的后一个字符为开头
#用列表存储时间复杂度是O(n^3)，用字典存储时间复杂度为O(n^2)
#结果：最后一项超时
###############################################
#列表存储
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max=0
        tmp=[]
        for  i in range(len(s)):
            tmp.append(s[i])
            for  j in range(i+1,len(s)):
                if s[j]  in tmp:
                    for k in range(len(tmp)):
                        if s[j] == tmp[k]:
                            i=i+k+1
                    if len(tmp)>max:
                        max=len(tmp)
                    tmp=[]
                    break
                else:
                    tmp.append(s[j])
                    if len(tmp)>max:
                        max=len(tmp)
        return max

#字典存储
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max=0
        tmp={}
        for  i in range(len(s)):
            tmp[s[i]]=i
            for  j in range(i+1,len(s)):
                if s[j]  in tmp:
                    i=tmp[s[j]]+1
                    if len(tmp)>max:
                        max=len(tmp)
                    tmp={}
                    break
                else:
                    tmp[s[j]]=j
                    if len(tmp)>max:
                        max=len(tmp)
        return max

############################################
#时间复杂度：O(n)
##########################################
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max=0
        curr=0
        last_start=0
        tmp={}
        for  i in range(len(s)):
            if s[i] in tmp:
                if curr>max:
                    max=curr
                if tmp[s[i]]+1>last_start:
                    last_start=tmp[s[i]]+1
                curr=i-last_start+1
                '''
                wrong：
                curr=i-tmp[s[i]]
                example:abba
                '''
                tmp[s[i]]=i  #更新重复的字符的位置
            else:
                tmp[s[i]]=i
                curr+=1
                
        if curr >max:
            max=curr
            
        return max