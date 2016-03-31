# encoding:utf-8
# 功能：将罗马数字转为阿拉伯数字
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        romaDict = {'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1}
        sum = 0
        
        if len(s) == 1:
            return romaDict[s]
        
        i = 0    
        while(i<len(s)-1):
            if romaDict[s[i]]<romaDict[s[i+1]]:
                value = romaDict[s[i+1]] - romaDict[s[i]]
                sum += value
                i+=2
            else:
                sum += romaDict[s[i]]
                i += 1
            
        # 最后一位可能还没被遍历
        if i < len(s):
            sum += romaDict[s[i]]
        return sum 