/**
* Author: WuLC
* Date:   2017-01-09 10:19:31
* Last modified by:   WuLC
* Last Modified time: 2017-01-09 10:26:54
* Email: liangchaowu5@gmail.com
*/

// deal with it in String
public class Solution 
{
    public String addBinary(String a, String b) 
    {
        String result = "";
        int m = a.length()-1, n = b.length()-1;
        int carrier = 0;
        while(m>=0 || n >=0)
        {
            if(m >= 0)  
            {
                carrier += a.charAt(m)-'0';
                m--;
            }
            if(n >= 0)  
            {
                carrier += b.charAt(n) -'0';
                n-- ;
            }
            
            result = String.valueOf(carrier%2) + result;
            carrier >>= 1;
        }
        if (carrier == 1) result = '1'+result; 
        return result;
    }
}

//deal with it in StringBuffer
public class Solution 
{
    public String addBinary(String a, String b) 
    {
        StringBuffer result = new StringBuffer();
        int m = a.length()-1, n = b.length()-1;
        int carrier = 0;
        while(m>=0 || n >=0)
        {
            if(m >= 0)  
            {
                carrier += a.charAt(m)-'0';
                m--;
            }
            if(n >= 0)  
            {
                carrier += b.charAt(n) -'0';
                n-- ;
            }
            
            result.append(String.valueOf(carrier%2));
            carrier >>= 1;
        }
        if (carrier == 1) result.append('1');
        result.reverse();
        return result.toString();
    }
}