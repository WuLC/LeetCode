/**
* Author: WuLC
* Date:   2016-10-25 16:27:39
* Last modified by:   WuLC
* Last Modified time: 2016-10-25 16:27:50
* Email: liangchaowu5@gmail.com
*/

public class Solution 
{
    private static final Map<Character, Character> map = new  HashMap<Character, Character>();
    static
    {
        map.put('(', ')');
        map.put('[', ']');
        map.put('{', '}');
    }
    public boolean isValid(String s) 
    {
        Stack<Character> stack = new Stack<Character>();
        char c = ' ';
        for (int i=0; i < s.length(); i++)
        {
            c = s.charAt(i);
            if (map.containsKey(c)) stack.push(c);
            else if (stack.isEmpty() || map.get(stack.pop()) != c) return false;
        }
        if (stack.isEmpty()) return true;
        else return false;
    }
}