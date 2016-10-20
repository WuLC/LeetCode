/**
* Author: WuLC
* Date:   2016-10-20 22:35:47
* Last modified by:   WuLC
* Last Modified time: 2016-10-20 22:36:03
* Email: liangchaowu5@gmail.com
*/

public class Solution 
{
    public int myAtoi(String str) 
    {
        str = str.trim();
        int len = str.length();
        int flag = 1;
        long result = 0;
        char c;
        for (int i=0;i<len;i++)
        {
            c = str.charAt(i);
            if (c >= '0' && c <= '9')
            {
                result = result*10 + c - '0';
                if (result > Integer.MAX_VALUE) // long will also overflow,so just stop as the number  overflows range of interger
                    break;
            }
            else if (i==0 && c=='-')
                flag = -1;
            else if (i==0 && c=='+')
                continue;
            else
                break; //"12 3" should return 12
        }
        result *= flag;
        // rules for atoi
        if (result<=Integer.MIN_VALUE) return Integer.MIN_VALUE;
        else if (result>=Integer.MAX_VALUE) return Integer.MAX_VALUE;
        else return Math.toIntExact(result);
    }
}