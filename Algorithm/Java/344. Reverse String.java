/**
* Author: LC
* Date:   2017-01-31 23:16:01
* Last modified by:   WuLC
* Last Modified time: 2017-01-31 23:16:14
* Email: liangchaowu5@gmail.com
*/


public class Solution 
{
    public String reverseString(String s) 
    {
        StringBuffer result = new StringBuffer();
        for(int i=s.length()-1;i>=0;i--) result.append(s.charAt(i));
        return result.toString();
    }
}