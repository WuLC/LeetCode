/*
 * Created on Sat Nov 04 2017 20:21:42
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

// a little trick, minus 1 from n for each iteration
class Solution 
{
    public String convertToTitle(int n) 
    {
        StringBuilder result = new StringBuilder();
        while(n != 0)
        {
            n -= 1;
            result.append((char)(65 + n%26));
            n /= 26;
        }
        return result.reverse().toString();
    }
}