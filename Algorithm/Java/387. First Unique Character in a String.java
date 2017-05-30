/*
* @Author: WuLC
* @Date:   2017-05-30 13:09:13
* @Last Modified by:   WuLC
* @Last Modified time: 2017-05-30 13:09:22
* @Email: liangchaowu5@gmail.com
*/

// hashmap
public class Solution 
{
    public int firstUniqChar(String s) 
    {
        Map<Character, Integer> count = new HashMap<Character, Integer>();
        for(int i = 0; i < s.length(); i++)
        {
            char c = s.charAt(i);
            if (!count.containsKey(c)) count.put(c, 0);
            count.put(c, count.get(c)+1);
        }
        for(int i = 0; i < s.length(); i++)
        {
            if(count.get(s.charAt(i)) == 1) return i;
        }
        return -1;
    }
}