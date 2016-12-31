/**
* Author: WuLC
* Date:   2016-12-31 20:45:29
* Last modified by:   WuLC
* Last Modified time: 2016-12-31 20:48:35
* Email: liangchaowu5@gmail.com
*/

// use trim method to remove leading and trailing whitespace
// operate on the string or change it to char array
public class Solution 
{
    public int lengthOfLastWord(String s) 
    {
        s = s.trim();
        int count = 0, idx = s.length()-1;
        while(idx >= 0)
        {
            if (s.charAt(idx) == ' ') return count;
            count++;
            idx--;
        }
        return count;
    }
}

// turn string to char array
public class Solution 
{
    public int lengthOfLastWord(String s) 
    {
        s = s.trim();
        int count = 0, idx = s.length()-1;
        char[] chars = s.toCharArray();
        while(idx >= 0)
        {
            if (chars[idx] == ' ') return count;
            count++;
            idx--;
        }
        return count;
    }
}