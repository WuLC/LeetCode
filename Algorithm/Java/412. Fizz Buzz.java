/**
* Author: WuLC
* Date:   2017-02-01 23:36:49
* Last modified by:   WuLC
* Last Modified time: 2017-02-01 23:37:45
* Email: liangchaowu5@gmail.com
*/


public class Solution 
{
    public List<String> fizzBuzz(int n) 
    {
        List<String> result = new ArrayList<String>();
        String tmp;
        for(int i=1; i<=n; i++)
        {
            tmp="";
            if( i%3 == 0 ) tmp+="Fizz";
            if( i%5 == 0 ) tmp+="Buzz";
            if(tmp.length() == 0) tmp+=String.valueOf(i);
            result.add(tmp);
        }
        return result;
    }
}