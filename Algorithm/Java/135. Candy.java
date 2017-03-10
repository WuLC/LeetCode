/**
* Author: LC
* Date:   2017-03-11 00:08:20
* Last modified by:   WuLC
* Last Modified time: 2017-03-11 00:09:49
* Email: liangchaowu5@gmail.com
*/

//traverse the ratings in two directions and caculate according to there neighbor ratings
public class Solution 
{
    public int candy(int[] ratings) 
    {
        int n = ratings.length;
        if (n==0) return 0;
        int[] count = new int[n];
        Arrays.fill(count, 1);
        for(int i=1; i<n; i++)
        {
            if(ratings[i] > ratings[i-1]) 
                count[i] = count[i-1] + 1;
        }
        for(int i=n-2; i >= 0; i--)
        {
            if(ratings[i] > ratings[i+1] && count[i+1] >= count[i]) 
                count[i] = count[i+1] + 1;
        }
        int result = 0;
        for(int tmp : count)
            result += tmp;
        return result;
    }
}