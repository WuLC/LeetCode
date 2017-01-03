/**
* Author: WuLC
* Date:   2017-01-03 20:19:18
* Last modified by:   WuLC
* Last Modified time: 2017-01-03 20:20:50
* Email: liangchaowu5@gmail.com
*/

// naive solution using stack
public class Solution 
{
    public int[] plusOne(int[] digits) 
    {
        Stack<Integer> stack = new Stack<Integer>();
        int carry = 1, tmp, currDigit;
        for(int i=digits.length - 1; i>=0; i--)
        {
            tmp = carry + digits[i];
            carry = tmp/10;
            currDigit = tmp%10;
            stack.push(currDigit);
        }
        if (carry!=0) stack.push(carry);
        
        int[] result = new int[stack.size()];
        int idx = 0;
        while (!stack.isEmpty()) result[idx++] = stack.pop();
        return result;
    }
}


// referered fast solution
public class Solution 
{
    public int[] plusOne(int[] digits) 
    {
        int n = digits.length;
        for(int i=n-1; i>=0; i--) 
        {
            if(digits[i] < 9) 
            {
                digits[i]++;
                return digits;
            }
            
            digits[i] = 0;
        }
        
        int[] newNumber = new int [n+1];
        newNumber[0] = 1;
        
        return newNumber;
    }
}