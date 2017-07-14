/*
* @Author: WuLC
* @Date:   2017-07-14 21:42:55
* @Last Modified by:   WuLC
* @Last Modified time: 2017-07-14 21:43:26
* @Email: liangchaowu5@gmail.com
*/

// pay attention to both positive and negative numbers
public class Solution 
{
    public String convertToBase7(int num) 
    {
        if (num == 0) return "0";
        String flag = "";
        if(num < 0)
        {
            flag = "-";
            num *= -1;
        }
        StringBuilder s  = new StringBuilder();
        while (num > 0)
        {
            s.append(String.valueOf(num%7));
            num /= 7;
        }
        return flag+s.reverse().toString();    
    }
}