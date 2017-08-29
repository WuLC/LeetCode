/*
* @Author: LC
* @Date:   2017-08-26 12:31:56
* @Last Modified by:   LC
* @Last Modified time: 2017-08-29 23:05:07
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


// stackoverflow
class Solution 
{
    public int longestSubstring(String s, int k) 
    {
        int[] count = new int[26];
        for(int i = 0; i < s.length(); i++)
        {
            char c = s.charAt(i);
            count[c - 'a'] += 1;
        }
        for (int i = 0 ; i < 26; i++)
        {
            if(count[i] > 0 && count[i] < k)
            {
                for(int j = 0; j < s.length(); j++)
                {
                    if (s.charAt(j) == i +'a')
                    return Math.max(longestSubstring(s.substring(0, i), k), longestSubstring(s.substring(i+1, s.length()), k));
                }
            }
        }
        return s.length();
    }
}

// AC
class Solution 
{
    public int longestSubstring(String s, int k) 
    {
        char[] chars = s.toCharArray();
        return helper(chars, 0, chars.length - 1, k);
    }
    
    public int helper(char[] chars, int start, int end, int k)
    {
        if (end - start + 1 < k) return 0;
        int[] count = new int[26];
        for(int i = start; i <= end; i++) count[chars[i] - 'a'] += 1;
        for(int i = 0; i < 26; i++)
        {
            if (count[i] > 0 && count[i] < k)
            {
                for(int j = start; j <= end; j++)
                    if (chars[j] == 'a' + i) return Math.max(helper(chars, start, j-1, k), helper(chars, j+1, end, k));
            }
        }
        return end - start + 1;
    }
}