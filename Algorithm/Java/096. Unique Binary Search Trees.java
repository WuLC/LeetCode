/*
* @Author: WuLC
* @Date:   2017-06-20 10:26:55
* @Last Modified by:   WuLC
* @Last Modified time: 2017-06-20 10:27:27
* @Email: liangchaowu5@gmail.com
*/

// recursive with cache
public class Solution 
{
    private Map<Integer, Integer> cache = new HashMap<Integer, Integer>(); // TLE without cache
    public int numTrees(int n) 
    {
        if (cache.containsKey(n)) return cache.get(n);
        if (n <= 1) return n;
        int count = 0, left, right;
        for (int i = 0; i < n; i++)
        {
            left = numTrees(i);
            right = numTrees(n-i-1);
            if (left != 0 && right != 0) count += left * right;
            else count += left+right;
        }
        cache.put(n, count);
        return count;
    }
}