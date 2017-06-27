/*
* @Author: WuLC
* @Date:   2017-06-27 17:40:18
* @Last Modified by:   WuLC
* @Last Modified time: 2017-06-27 17:40:28
* @Email: liangchaowu5@gmail.com
*/


// stack
public class Solution 
{
    public int evalRPN(String[] tokens) 
    {
        Stack<Integer> nums = new Stack<Integer>();
        for (String s : tokens)
        {
            if (s.equals("+")) nums.push(nums.pop() + nums.pop());
            else if(s.equals("-")) nums.push(-nums.pop() + nums.pop());
            else if(s.equals("*")) nums.push(nums.pop() * nums.pop());
            else if(s.equals("/")) 
            {
                int a = nums.pop();
                int b = nums.pop();
                nums.push(b/a);
            }
            else nums.push(Integer.valueOf(s));
        }
        return nums.pop();
    }
}