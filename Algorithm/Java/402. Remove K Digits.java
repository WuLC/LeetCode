/*
 * Created on Wed Mar 14 2018 0:5:51
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

// stack
class Solution 
{
    public String removeKdigits(String num, int k) 
    {
        Stack<Character> stack = new Stack<Character>();
        if (k==num.length()) return "0";
        int count = 0;
        for(int i = 0; i < num.length(); i++)
        {
            while (!stack.empty() && stack.peek() > num.charAt(i) && count < k)
            {
                stack.pop();
                count++;
            }
            stack.push(num.charAt(i));
        }
        while (count < k)
        {
            stack.pop();
            count++;
        }
        StringBuilder sb = new StringBuilder();
        while (!stack.empty()) sb.append(stack.pop());
        sb.reverse();
        while(sb.length() > 1 && sb.charAt(0)=='0') sb.deleteCharAt(0);
        return sb.toString();
    }
}