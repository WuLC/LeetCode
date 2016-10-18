/**
* Author: LC
* Date:   2016-10-18 17:36:30
* Last modified by:   WuLC
* Last Modified time: 2016-10-18 17:46:29
* Email: liangchaowu5@gmail.com
*/

// method 1
// turn the number to string and then judge
public class Solution 
{
    public boolean isPalindrome(int x) 
    {
        String s = String.valueOf(x);
        int i = 0, j = s.length() - 1;
        while (i < j)
        {
            if (s.charAt(i++) != s.charAt(j--))
                return false;
        }
        return true;
    }
}


// method 2
// operate on the number, just take and reverse the lower half of the number
public class Solution 
{
    public boolean isPalindrome(int x) 
    {
        if (x < 0 || x > 0 && x%10 == 0) return false;
        int tmp = 0;
        while (x > tmp)
        {
            tmp = tmp * 10 + x%10;
            x /= 10;
        }
        return (x == tmp || x == tmp/10);
    }
}