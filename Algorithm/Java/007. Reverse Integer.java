/**
* Author: WuLC
* Date:   2016-10-20 20:55:42
* Last modified by:   WuLC
* Last Modified time: 2016-10-20 20:56:21
* Email: liangchaowu5@gmail.com
*/

public class Solution 
{
    public int reverse(int x) 
    {
        int flag = 1;
        String s = String.valueOf(x);
        if (x < 0) 
        {
            flag = -1;
            s = s.substring(1); // remove the first character -
        }
        
        long n = flag * Long.parseLong(new StringBuffer(s).reverse().toString());
        if (n<=Integer.MAX_VALUE && n >= Integer.MIN_VALUE)
            return Math.toIntExact(n); // throw Exception when overflows
        else
            return 0;
    }
}