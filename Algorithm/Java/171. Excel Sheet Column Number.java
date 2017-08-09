/*
* @Author: WuLC
* @Date:   2017-08-09 16:51:19
* @Last Modified by:   WuLC
* @Last Modified time: 2017-08-09 16:56:56
* @Email: liangchaowu5@gmail.com
*/


// 26 进制
public class Solution 
{
    public int titleToNumber(String s) 
    {
        int result = 0, n = s.length();
        char[] chars = s.toCharArray();
        for(int i = n - 1; i >= 0; i--)
            result += Math.pow(26, n-i-1) * (chars[i] - 'A' + 1);
        return result;
    }
}