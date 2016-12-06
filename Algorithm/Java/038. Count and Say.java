/**
* Author: WuLC
* Date:   2016-12-06 18:06:36
* Last modified by:   WuLC
* Last Modified time: 2016-12-06 18:09:35
* Email: liangchaowu5@gmail.com
*/


// with helper function to count the original number and return it as string
// don't transfer to integer since there may be overflow 
public class Solution {
    public String countAndSay(int n) 
    {
        String result = "";
        for (int i=0;i<n;i++)
        {
            if (i==0) result = "1";
            else result = helper(result);
        }
        return result;
    }
    
    public String helper(String s)
    {
        StringBuilder str = new StringBuilder();
        int left = 0, right = 0;
        while (right < s.length())
        {
            if (right+1 < s.length() && s.charAt(right) == s.charAt(right+1)) right += 1;
            else
            {
                str.append((char)(right-left+1+48)); // ascii number of the digit
                str.append(s.charAt(left));
                left = right = right+1;
            }
        }
        return str.toString();
    }
}