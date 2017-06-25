/*
* @Author: WuLC
* @Date:   2017-06-25 16:17:35
* @Last Modified by:   WuLC
* @Last Modified time: 2017-06-25 16:17:56
* @Email: liangchaowu5@gmail.com
*/


// greedy

public class Solution 
{
    public String removeDuplicateLetters(String s) 
    {
        Stack<Character> chars = new Stack<Character>();
        Map<Character, Integer> count = new HashMap<Character, Integer>();
        int[] stored = new int[26];
        Arrays.fill(stored, 0);
        
        char[] c = s.toCharArray();
        for(int i = 0; i < c.length; i++)
        {
            if (!count.containsKey(c[i])) count.put(c[i], 0);
            count.put(c[i], count.get(c[i])+1);
        }
        
        for(int i = 0; i < c.length; i++)
        {
           if(stored[c[i] - 'a'] == 0)
           {
                while (chars.size() > 0 && chars.peek() > c[i] && count.get(chars.peek()) > 1)
                {
                    char tmp = chars.pop();
                    stored[tmp - 'a'] = 0;
                    count.put(tmp, count.get(tmp) - 1);
                }
                chars.push(c[i]);
                stored[c[i] -'a'] = 1;
            }
            else count.put(c[i], count.get(c[i]) - 1);
        }
        String result = "";
        while (chars.size() > 0)  result = chars.pop() + result;
        return result;
    }
}