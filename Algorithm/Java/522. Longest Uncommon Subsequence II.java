/**
* Author: WuLC
* Date:   2017-04-21 16:48:58
* Last modified by:   WuLC
* Last Modified time: 2017-04-21 17:04:00
* Email: liangchaowu5@gmail.com
*/

// time complexity: O(knlogn), k is the average length of strs and n is the length of strs
// use treemap, key is the length of strings that stored in its' value
public class Solution 
{
    public int findLUSlength(String[] strs) 
    {
        Set<String> duplicate = new HashSet<String>();
        Map<Integer, HashSet<String>> count = new TreeMap<Integer, HashSet<String>>();
        for(String str:strs)
        {
            if (duplicate.contains(str))  continue;
            int len = str.length();
            if (!count.containsKey(len))  count.put(len, new HashSet<String>());
            if (count.get(len).contains(str))
            {
                count.get(len).remove(str);
                duplicate.add(str);
            }
            else count.get(len).add(str);
        }
        
        // traverse the treemap reversely
        ArrayList<Integer> keys = new ArrayList<Integer>(count.keySet());
        for (int i=keys.size()-1; i>=0; i--)
        {
            int len = keys.get(i);
            boolean isSub;
            for (String s1:count.get(len))
            {
                isSub = false;
                for (String s2:duplicate)
                {
                    if (isSubsequence(s1, s2)) 
                    {
                        isSub = true;
                        break;
                    }
                }
                if (isSub==false) return len;
            }    
        }
        return -1;
    }
    
    
    public boolean isSubsequence(String s1, String s2) // judge if s1 is subsequence of s2
    {
        if (s1.length() > s2.length()) return false;
        // it seems faster to use charAt instead of transfer it to char array 
        int p1=0, p2=0;
        while (p1 < s1.length() && p2 < s2.length())
        {
            if (s1.charAt(p1) == s2.charAt(p2))
            {
                p1++;
                p2++;
            }
            else p2++;
        }
        if (p1==s1.length()) return true;
        else return false;
        /*
        char[] c1 = s1.toCharArray();
        char[] c2 = s2.toCharArray();
        int p1=0, p2=0;
        while (p1 < c1.length && p2 < c2.length)
        {
            if (c1[p1] == c2[p2])
            {
                p1++;
                p2++;
            }
            else p2++;
        }
        if (p1==c1.length) return true;
        else return false;
        */
    }
}