#encoding:utf-8
##############################
#将字符串转为数字，需要考虑的问题有
#1.去掉空格,且只能去掉字符串前面的空格
#2.非空格的第一个字符不是‘+’、‘-’或数字则视为不合法，返回0
#3.溢出整数的范围要返回整数范围的最大值(2^31-1)或最小值(-2^31) 
#4.整数字符串后可以跟上其他的字符串，忽略即可
##############################
class Solution(object):
    def myAtoi(self,str):
        """
        :type str:str
        :rtype :int
        """
        INT_MAX=2147483647
        INT_MIN=-2147483648
    
        result=''
        flag=1
        nonZero=0

        if len(str) ==0:
            return 0
        #remove the space
        i=0
        while i<len(str) and str[i].isspace():
            i+=1
        #judge possible initial flag
        if str[i]== '-':
            flag=-1
            i+=1
        elif str[i]=='+':
            i+=1
       
        for j in range(i,len(str)):
            if not str[j].isdigit(): 
                break
            #the single character must be a number below
            if nonZero==0 and str[j]=='0':
                continue
            elif nonZero==0 and str[j]!= '0':
                nonZero=1
                result+=str[j]
            elif nonZero==1:
                result+=str[j]

        if len(result)==0:
            return 0
        else:
            intResult=int(result)*flag
            if intResult >= INT_MAX:
                return INT_MAX
            elif intResult<= INT_MIN:
                return INT_MIN
            else:
                return intResult






