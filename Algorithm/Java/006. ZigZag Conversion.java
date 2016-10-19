/**
* Author: WuLC
* Date:   2016-10-19 22:32:34
* Last modified by:   WuLC
* Last Modified time: 2016-10-19 22:35:40
* Email: liangchaowu5@gmail.com
*/

public class Solution 
{
    public String convert(String s, int numRows) 
    {
        int inter;
        if (numRows==1) 
            inter = 1;
        else 
            inter = (numRows - 1)*2;
        String result = "";
        for (int i=0; i<numRows; i++)
        {
            int idx = i, tmp = (numRows - 1 - i)*2;;
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