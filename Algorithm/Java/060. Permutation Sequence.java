/**
* Author: WuLC
* Date:   2017-01-02 21:17:56
* Last modified by:   WuLC
* Last Modified time: 2017-01-02 21:26:03
* Email: liangchaowu5@gmail.com
*/


// locate each number bit by bit 
public class Solution 
{
    private String result;
    private int used;
    
    public String getPermutation(int n, int k) 
    {
        result = "";
        used = 0;
        dfs(n, k-1, 1);
        return result;
    }
    
    
    private void dfs(int n, int k, int m)
    {
        if (m>n) return;
        int tmp = factorial(n-m);
        int count = k/tmp, idx = 1, tmpCount = 0;
        k -= count*tmp;
        count += 1;
        for(; idx <= n; idx++)
        {
            if (((used>>idx) & 1) == 0) tmpCount++;
            if (tmpCount == count) break;
        }
        result += String.valueOf(idx);
        used ^= (1<<idx);
        dfs(n, k, m+1);
    }
    
    
    private int factorial(int n)
    {
        int fac = 1;
        for(int i=2; i<=n; i++) 
            fac *= i;
        return fac;
    }
}
