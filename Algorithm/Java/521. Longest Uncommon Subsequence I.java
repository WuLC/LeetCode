/**
* Author: WuLC
* Date:   2017-04-21 15:53:54
* Last modified by:   WuLC
* Last Modified time: 2017-04-21 15:54:59
* Email: liangchaowu5@gmail.com
*/


// if two strings are not equal, just return the longest string 
public class Solution
{
    public int findLUSlength(String a, String b) 
    {
        if (a.equals(b)) return -1;
        else return Math.max(a.length(), b.length());
    }
}