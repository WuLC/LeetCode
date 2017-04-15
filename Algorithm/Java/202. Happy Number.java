/**
* Author: WuLC
* Date:   2017-04-15 22:04:10
* Last modified by:   WuLC
* Last Modified time: 2017-04-15 22:04:51
* Email: liangchaowu5@gmail.com
*/

// use set to store appeared numbers
public class Solution 
{
    public boolean isHappy(int n) 
    {
        Set<Integer> appear = new HashSet<Integer>();
        String str = null;
        int tmp = n;
        while (true)
        {
            str = String.valueOf(tmp);
            tmp = 0;
            for(int i = 0; i < str.length(); i++)
                tmp += Math.pow(str.charAt(i) - '0', 2);
            if (tmp == 1) return true;
            else if (appear.contains(tmp)) return false;
            else appear.add(tmp);
        }
    }
}