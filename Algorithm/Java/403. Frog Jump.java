/*
* @Author: WuLC
* @Date:   2017-03-04 14:42:32
* @Last Modified by:   WuLC
* @Last Modified time: 2017-03-04 14:43:08
* @Email: liangchaowu5@gmail.com
*/

// naive dp, O(n^2) time, O(n^2) space
public class Solution 
{
    public boolean canCross(int[] stones) 
    {
        List<ArrayList<Integer>> steps = new ArrayList<ArrayList<Integer>>();
        for(int i=0; i<stones.length; i++)
        {
            ArrayList<Integer> tmp = new ArrayList<Integer>();
            if(i==0)  tmp.add(0);
            else if(i==1 && stones[i]-stones[i-1] == 1) tmp.add(1);
            else
            {
                for(int j=0; j<i; j++)
                {
                    ArrayList<Integer> currSteps = steps.get(j);
                    for(int k=0; k < currSteps.size(); k++)
                        if(Math.abs(currSteps.get(k) + stones[j] - stones[i]) <= 1)
                        {
                            tmp.add(stones[i]-stones[j]);
                            break;
                        }
                }
            }
            steps.add(tmp);
        }
        return steps.get(stones.length-1).size()!= 0;
    }
}