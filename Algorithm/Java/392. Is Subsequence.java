/*
 * Created on Sat Apr 07 2018 17:30:52
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

// simple solution, O(n) time, n is the length of t
class Solution 
{
    public boolean isSubsequence(String s, String t) 
    {
        if (s.length() == 0) return true;
        int idx = 0;
        for(int i=0; i<t.length(); i++)
        {
            if(t.charAt(i) == s.charAt(idx)) idx++;
            if(idx == s.length()) return true;
        }
        return false;
    }
}