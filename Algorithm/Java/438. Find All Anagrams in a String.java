/**
* Author: WuLC
* Date:   2017-04-21 20:32:01
* Last modified by:   WuLC
* Last Modified time: 2017-04-21 22:13:51
* Email: liangchaowu5@gmail.com
*/


// hashtable and two pointers
// time complexity: O(n), n is the length of the s
public class Solution 
{
    public List<Integer> findAnagrams(String s, String p) 
    {
        ArrayList<Integer> indices = new ArrayList<Integer>();
        int sLen = s.length(), pLen = p.length();
        if (sLen < pLen) return indices;
        HashMap<Character, Integer> count = new HashMap<Character, Integer>();
        for(int i=0; i < pLen; i++)
        {
            char c = p.charAt(i);
            if(!count.containsKey(c)) count.put(c, 0);
            count.put(c, count.get(c) + 1);
        }
        
        int p1 = 0, p2 = 0;
        HashMap<Character, Integer> tmp = new HashMap<Character, Integer>();
        while(p2 < sLen)
        {
            char c = s.charAt(p2);
            if (!count.containsKey(c))
            {
                p1 = p2+1;
                p2 = p1;
                tmp.clear();
            }
            else
            {
                if (!tmp.containsKey(c)) tmp.put(c, 0);
                tmp.put(c, tmp.get(c)+1);
                
                while (tmp.get(c) > count.get(c))
                {
                    tmp.put(s.charAt(p1), tmp.get(s.charAt(p1))-1);
                    p1++;
                }
            
                if( p2 - p1 + 1 == pLen) 
                {
                    indices.add(p1);
                    tmp.put(s.charAt(p1), tmp.get(s.charAt(p1))-1);
                    p1++;
                }
                p2++;
            }

        }
        return indices;
    }
}