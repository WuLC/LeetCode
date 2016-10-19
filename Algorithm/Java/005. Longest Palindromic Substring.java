/**
* Author: LC
* Date:   2016-10-19 21:03:00
* Last modified by:   WuLC
* Last Modified time: 2016-10-19 21:05:32
* Email: liangchaowu5@gmail.com
*/

//take each character as the center of the palindrome substring and expand it in two directions
//pay attention the substring can be odd or even

public class Solution 
{

    public String longestPalindrome(String s) 
    {
        String result = "", tmp;
        for (int i=0; i < s.length(); i++)
        {
            tmp = oddLongest(s, i);
            if (tmp.length() > result.length()) result = tmp;
            tmp = evenLongest(s, i);
            if (tmp.length() > result.length()) result = tmp;
        }
        return result;
    }

    public String oddLongest(String s, int index)
    {
        int i=index, j=index, len = s.length()-1;
        while (i>=0 && j<=len && s.charAt(i) == s.charAt(j))
        {
            i--;
            j++;
        }
        return s.substring(i+1,j);
    }
    
    public String evenLongest(String s, int index)
    {
        int i=index, j=index+1, len = s.length()-1;
        while (i>=0 && j<=len && s.charAt(i) == s.charAt(j))
        {
            i--;
            j++;
        }
        if (i+1==j) 
            return "";
        else
            return s.substring(i+1,j);
    }
}