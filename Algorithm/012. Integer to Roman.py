# encoding:utf-8
'''
功能：将阿拉伯数字转为罗马数字，下面为具体规则：

1.罗马数字共有7个，即I（1）、V（5）、X（10）、L（50）、C（100）、D（500）和M（1000）
2.在较大的罗马数字的右边记上较小的罗马数字，表示大数字加小数字。
3.在较大的罗马数字的左边记上较小的罗马数字，表示大数字减小数字。
4.左减的数字有限制，仅限于I、X、C。比如45不可以写成VL，只能是XLV
5.但是，左减时不可跨越一个位值。比如，99不可以用IC（100 - 1）表示，而是用XCIX（[100 - 10] + [10 - 1]）表示。（等同于阿拉伯数字每位数字分别表示。）
6.左减数字必须为一位，比如8写成VIII，而非IIX。
7.右加数字不可连续超过三位，比如14写成XIV，而非XIIII。

'''
class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        result = ''
        
        if num>=1000:
            n = num/1000
            for i in range(n):
                result += 'M'
            num -= 1000*n
         
        if num>=900:
            num -= 900
            result += 'CM'
            
            
        if num>=500:
            n = num/500
            for i in range(n):
                result += 'D'
            num -= 500
        '''
        下面的判断错误，490应该表示为(500-100)+(100-10)
        if num>=490:
            num -= 490
            result += 'XD'
        '''    
        
        if num >= 400:
            num -= 400
            result += 'CD'
        
        if num >= 100:
            n = num /100
            for i in range(n):
                result += 'C'
            num -= 100*n
        
        if num >= 90:
            num -= 90
            result += 'XC'

        if num >= 50:
            n = num /50
            for i in range(n):
                result += 'L'
            num -= 50*n
        
        if num >= 40:
            num -= 40
            result += 'XL'

        if num >= 10:
            n = num / 10
            for i in range(n):
                result+='X'
            num -= n*10
        # num 已经 <= 10
        if num >= 9:
            num -= 9
            result += 'IX'
            
        if num >= 5:
            result += 'V'
            num -= 5
            
        if num >=4:
            result += 'IV'
            num -= 4
        
        if num >0:
            for i in range(num):
                result += 'I'
        
        return result