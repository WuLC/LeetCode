/*
* @Author: WuLC
* @Date:   2017-02-27 17:28:36
* @Last Modified by:   WuLC
* @Last Modified time: 2017-02-27 17:31:03
* @Email: liangchaowu5@gmail.com
*/


//naive solution, check factor one by one 
public class Solution 
{
    public boolean isUgly(int num) 
    {
        if (num == 0) return false;
        while(num%5 == 0) num/=5;
        while(num%3 == 0) num/=3;
        while(num%2 == 0) num/=2;
        return num==0;
    }
}