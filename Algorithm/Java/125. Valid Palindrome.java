/**
* Author: WuLC
* Date:   2016-10-15 22:17:08
* Last modified by:   WuLC
* Last Modified time: 2016-10-15 22:25:39
* Email: liangchaowu5@gmail.com
*/

public class Solution 
{
    public boolean isPalindrome(String s) 
    {
        int left = 0, right = s.length() - 1;
        while (left < right)
        {
            while (left < right && !Character.isLetterOrDigit(s.charAt(left)))  left ++;
            while (left < right && !Character.isLetterOrDigit(s.charAt(right))) right --;
            if(Character.toLowerCase(s.charAt(left)) != Character.toLowerCase(s.charAt(right)))
                return false;
            left ++;right --;
        }
        return true;
    }
}