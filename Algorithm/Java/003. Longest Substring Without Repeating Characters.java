/**
* Author: WuLC
* Date:   2016-10-11 21:51:20
* Last modified by:   WuLC
* Last Modified time: 2016-10-11 21:51:51
* Email: liangchaowu5@gmail.com
*/


// Two pointers and Hash table
public class Solution 
{
    public int lengthOfLongestSubstring(String s) 
    {
        
        HashMap<Character, Integer> indices = new HashMap<Character, Integer>();
        char curr = 't';
        int left = 0, right = 0, result = 0;
        while (right < s.length())
        {
            curr = s.charAt(right);
            if (indices.containsKey(curr) && indices.get(curr) >= left)
            {
                result = Math.max(right - left, result);
                left = indices.get(curr) + 1;
            }
            indices.put(curr, right);
            right ++;
        }
        return Math.max(result, right - left);
    }
}