/**
* Author: LC
* Date:   2016-11-06 09:55:32
* Last modified by:   WuLC
* Last Modified time: 2016-11-06 12:42:14
* Email: liangchaowu5@gmail.com
*/


// naive solution
// O(mn) time, O(mn) space
public class Solution 
{
    public int strStr(String haystack, String needle) 
    {
        int haystackLength = haystack.length(), needleLength = needle.length();
        for (int i=0;i <= haystackLength - needleLength; i++)
        {
            if (haystack.substring(i, i + needleLength).equals(needle))  return i;
        }
        return -1;
    }
}

// naive solution
// O(mn) time, O(1) space
public class Solution 
{
    public int strStr(String haystack, String needle) 
    {
        int haystackLength = haystack.length(), needleLength = needle.length(), i=0, j=0, tmp;
        if (needleLength==0) return 0;
        while (i < haystackLength)
        {
            tmp = i;
            j = 0;
            while (tmp < haystackLength && j < needleLength)
            {
                if (haystack.charAt(tmp) == needle.charAt(j))
                {
                    tmp++; 
                    j++;
                }
                else break;
            }
            if (j==needleLength) return i;
            i++;
        }
        return -1;
    }
}

//another more concise solution
public class Solution 
{
    public int strStr(String haystack, String needle) 
    {
        for (int i=0;;i++)
        {
            for(int j =0;;j++)
            {
                if (j==needle.length()) return i;
                if (i+j==haystack.length()) return -1;
                if (haystack.charAt(i+j)!=needle.charAt(j)) break;
            }
        }
    }
}

// KMP solution
// http://www.ruanyifeng.com/blog/2013/05/Knuth%E2%80%93Morris%E2%80%93Pratt_algorithm.html