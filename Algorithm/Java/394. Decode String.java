/*
* @Author: WuLC
* @Date:   2017-06-23 20:27:18
* @Last Modified by:   WuLC
* @Last Modified time: 2017-06-23 20:27:40
* @Email: liangchaowu5@gmail.com
*/


// stack
public class Solution 
{
    public String decodeString(String s)
    {
        Stack<Integer> nums = new Stack<Integer>();
        Stack<String> strs = new Stack<String>();
        char[] c = s.toCharArray();
        int index = 0;
        String curr = "", num = "";
        while (index < c.length)
        {
            if (Character.isDigit(c[index]))
            {
                num = "";
                while (index < c.length && Character.isDigit(c[index]))
                {
                    num += c[index];
                    index += 1;
                }
            }
            
            if (c[index] == '[')
            {
                nums.push(Integer.valueOf(num));
                strs.push(curr);
                curr = "";
            }
            else if(c[index] == ']')
            {
                int n = nums.pop();
                curr = new String(new char[n]).replace("\0", curr); // repeat for n time
                curr = strs.pop()+curr;
            }
            else curr += c[index];
            index += 1;
        }
        return curr;
    }
}