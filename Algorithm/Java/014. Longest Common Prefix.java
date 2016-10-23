/**
* Author: WuLC
* Date:   2016-10-23 12:04:09
* Last modified by:   WuLC
* Last Modified time: 2016-10-23 12:16:46
* Email: liangchaowu5@gmail.com
*/

// method 1, find the shortest length of strs firstly
public class Solution 
{
    public String longestCommonPrefix(String[] strs) 
    {
        if (strs.length==0) return "";
        StringBuffer longestPrefix = new StringBuffer();
        int longestLength = Integer.MAX_VALUE;
        for(String s:strs) longestLength = Math.min(longestLength, s.length());
        for(int i=0; i<longestLength; i++)
        {
            char c = strs[0].charAt(i);
            for (String s:strs)
            {
                if (s.charAt(i) != c) return longestPrefix.toString();
            }
            longestPrefix.append(c);
        }
        return longestPrefix.toString(); // identical strs 
    }
}


// method 2, don't find the shortest length of strs, but the code is not concise
public class Solution 
{
    public String longestCommonPrefix(String[] strs) 
    {
        if (strs.length==0) return "";
        StringBuffer longestPrefix = new StringBuffer();
        int idx = 0;
        boolean exceed = false;
        while (true)
        {
            char c = ' ';
            for(int i = 0; i<strs.length; i++)
            {
                if (idx < strs[i].length())
                {
                    if (i==0) c = strs[i].charAt(idx);
                    else if (c != strs[i].charAt(idx))
                    {
                        exceed = true;
                        break;
                    }
                }
                else
                {
                    exceed = true;
                    break;
                }
            }
            if (exceed)   return longestPrefix.toString();
            if (c != ' ') longestPrefix.append(c);
            idx += 1;
        }
        
    }
}


