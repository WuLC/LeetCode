/*
* @Author: WuLC
* @Date:   2017-02-28 13:38:38
* @Last Modified by:   WuLC
* @Last Modified time: 2017-02-28 13:39:13
* @Email: liangchaowu5@gmail.com
*/


// referer: https://discuss.leetcode.com/topic/21882/my-16ms-c-dp-solution-with-short-explanation
public class Solution
{
    public int nthUglyNumber(int n) 
    {
        int[] idices = {0,0,0};
        int[] primes = {2,3,5};
        ArrayList<Integer> uglies = new ArrayList<Integer>();
        uglies.add(1);
        while (uglies.size() < n)
        {
            int tmp = Math.min(uglies.get(idices[0])*primes[0], Math.min(uglies.get(idices[1])*primes[1], uglies.get(idices[2])*primes[2]));
            if(uglies.get(uglies.size()-1) < tmp) uglies.add(tmp);
            for(int i=0; i<3; i++)
            {
                if( uglies.get(idices[i])*primes[i] == tmp ) 
                    idices[i]++;
                    
            }
        }
        return uglies.get(n-1);
    }
}