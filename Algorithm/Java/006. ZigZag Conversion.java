/**
* Author: WuLC
* Date:   2016-10-19 22:32:34
* Last modified by:   WuLC
* Last Modified time: 2016-10-20 07:59:25
* Email: liangchaowu5@gmail.com
*/


// O(1) space, O(n) time
// charAt() is a constant-time operation.
public class Solution 
{
    public String convert(String s, int numRows) 
    {
        if (numRows==1) 
            return s;
        int inter = (numRows - 1)*2;
        String result = "";
        for (int i=0; i<numRows; i++)
        {
            int idx = i, tmp = (numRows - 1 - i)*2;
            while (idx < s.length())
            {
                result += s.charAt(idx);
                if (tmp == 0) tmp = inter;
                idx += tmp;
                tmp = inter - tmp;
            }
        }
        return result; 
    }
}


//O(n) space, O(n) time
public class Solution 
{
    public String convert(String s, int numRows) 
    {
        char[] c = s.toCharArray();
        StringBuffer[]  rows = new StringBuffer[numRows];
        for (int i = 0; i<numRows; i++) rows[i] = new StringBuffer();
        int idx = 0, len = s.length();
        while (idx < len)
        {
            for (int i=0; idx < len && i < numRows; i++)
                rows[i].append(s.charAt(idx++));
            for(int i=numRows-2; idx < len && i > 0; i--)
                rows[i].append(s.charAt(idx++));
        }
        for (int i=1; i< numRows; i++)
        {
            rows[0].append(rows[i]);
        }
        return rows[0].toString();
    }
}