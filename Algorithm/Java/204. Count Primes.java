/*
* @Author: WuLC
* @Date:   2017-07-07 22:01:55
* @Last Modified by:   WuLC
* @Last Modified time: 2017-07-09 09:20:00
* @Email: liangchaowu5@gmail.com
*/


// dp, TLE
public class Solution 
{
    private List<Integer> dp = new ArrayList<Integer>();
    public int countPrimes(int n) 
    {
        if (n == 0) return 0;
        for(int i = dp.size(); i < n; i++)
        {
            if (i <= 1) dp.add(0);
            else if(isPrime(i)) dp.add(dp.get(i-1) + 1);
            else dp.add(dp.get(i - 1));
        }
        return dp.get(n-1);
    }
    
    public boolean isPrime(int num)
    {
        for(int i = 2; i <= (int) Math.floor(Math.sqrt(num)); i++)
            if (num % i == 0) return false;
        return true;
    }
}


// referer: https://discuss.leetcode.com/topic/13654/my-simple-java-solution
public class Solution 
{
    public int countPrimes(int n) 
    {
        int[] isPrime = new int[n];
        Arrays.fill(isPrime, 1);
        int count = 0;
        for(int i = 2; i < n; i++)
        {
            if (isPrime[i] == 1)
            {
                count++;
                for(int j = 2; i * j < n; j++)
                    isPrime[i*j] = 0;
            }
        }
        return count;
    }
}