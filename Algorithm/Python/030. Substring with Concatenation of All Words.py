# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2016-04-04 11:02:34
# @Last modified by:   LC
# @Last Modified time: 2016-04-10 16:22:57
# @Email: liangchaowu5@gmail.com


# 列了两种方法作对比，一种超时，一种AC；对比过才能发现第二种方法的巧妙 

# 方法一，时间复杂度O(n^2)，n=len(s);提交超时
class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        # 注意words中的词可能会重复
        wordDict = {}
        for word in words:
            if word in wordDict:
                wordDict[word] += 1
            else:
                wordDict[word] = 1
        
        wordLen = len(words[0])
        result = []
        
        for i in range(len(s)-wordLen*wordNum+1):
            tmp = s[i:i+wordLen]
            tmpDict = {} # 存储words的临时list
            if tmp in words:                
                head = i
                while tmp in words and i < len(s)-wordLen+1:            
                    if tmp in tmpDict:
                        tmpDict[tmp] += 1
                    else:
                        tmpDict[tmp] = 1
                    
                    if tmpDict[tmp] > wordDict[tmp]:
                        tmpDict[tmp] -= 1
                        break

                    i += wordLen
                    tmp = s[i:i+wordLen]
                if tmpDict == wordDict:
                    result.append(head)
            else:
                continue         
        return result
 

# 方法二，时间复杂度O(n),n=len(s),能够AC         
class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        # 注意words中的词可能会重复
        wordDict = {}
        for word in words:
            if word in wordDict:
                wordDict[word] += 1
            else:
                wordDict[word] = 1
        
        wordLen = len(words[0])
        wordNum = len(words)
        wordSet = set(words)
        sLen = len(s)
        result = []
        
        for i in range(wordLen): 
            left = i
            tmpDict = {}
            count = 0
            j=i
            while j < sLen-wordLen+1: 
                tmp = s[j:j+wordLen]
                j += wordLen
                if tmp in wordSet:
                    if tmp in tmpDict:
                        tmpDict[tmp]+=1
                    else:
                        tmpDict[tmp]=1
                    
                    if tmpDict[tmp]<=wordDict[tmp]:
                        count+=1
                    else:
                        # 某个词的数量比wordDict中规定的要多了，在左边往右移动指针
                        while tmpDict[tmp] > wordDict[tmp]:
                            t = s[left:left+wordLen]
                            left += wordLen
                            tmpDict[t] -= 1
                            if tmpDict[t] < wordDict[t]:
                                count -= 1
                    # 仅去掉最左边的一个word，再往右找
                    if count == wordNum:
                        result.append(left)
                        t = s[left:left+wordLen]
                        tmpDict[t] -= 1
                        left += wordLen
                        count -= 1  
                # 当前的词不在wordDict                        
                else:
                    tmpDict = {}
                    count = 0 
                    left = j
        return result