/*
* @Author: LC
* @Date:   2017-08-26 12:31:56
* @Last Modified by:   LC
* @Last Modified time: 2017-08-26 12:32:05
*/

// TLE
class Solution 
{
    public int longestSubstring(String s, int k) 
    {
        Map<Character, Integer> count = new HashMap<Character, Integer>();
        for(int i = 0; i < s.length(); i++)
        {
            char c = s.charAt(i);
            if(!count.containsKey(c)) count.put(c, 0);
            count.put(c, count.get(c)+1);
        }
        int result = 0;
        boolean split = false;
        for (Map.Entry<Character, Integer> entry: count.entrySet())
        {
            if(entry.getValue() < k)
            {
                split = true;
                for(String part: s.split(String.valueOf(entry.getKey())))
                    result = Math.max(result, longestSubstring(part, k));
            }
        }
        if (split == true) return result;
        else return s.length();
    }
}