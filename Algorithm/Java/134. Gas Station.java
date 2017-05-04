/**
* Author: WuLC
* Date:   2017-05-05 00:30:51
* Last modified by:   WuLC
* Last Modified time: 2017-05-05 00:33:35
* Email: liangchaowu5@gmail.com
*/

// O(n) time, one important principle is that 
// if car starts at A and can not reach B. Any station between A and B can not reach B
public class Solution 
{
    public int canCompleteCircuit(int[] gas, int[] cost) 
    {
        int currGas = 0, idx = 0, tmp;
        while (idx < gas.length)
        {
            int i = 0;
            for(i = 0; i < gas.length; i++)
            {
                tmp = (i+idx)%gas.length;
                currGas += (gas[tmp] - cost[tmp]);
                if (currGas < 0)
                {
                    idx += i+1;
                    currGas = 0;
                    break;
                }
            }
            if (i == gas.length) return idx;
        }
        return -1;
    }
}