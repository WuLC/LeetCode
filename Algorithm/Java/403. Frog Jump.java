/*
* @Author: WuLC
* @Date:   2017-03-04 14:42:32
* @Last Modified by:   WuLC
* @Last Modified time: 2017-03-04 21:14:38
* @Email: liangchaowu5@gmail.com
*/

// dp, dp[i] represents the last steps that can reach position i
// time: average O(n^2), worst O(n^3)
// space:O(n^2) 
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


// dp, dp[i] represents the steps that position i can reach
// time: average O(n), worst O(n^2)
// space: O(n)
public class Solution 
{
    public boolean canCross(int[] stones) 
    {
        HashMap<Integer, HashSet<Integer>> steps = new HashMap<Integer, HashSet<Integer>>();
        for(int i=0; i < stones.length; i++)
            steps.put(stones[i], new HashSet<Integer>());
        steps.get(0).add(1);
        for(int i=0; i < stones.length; i++)
        {
            for(int step : steps.get(stones[i]))
            {
                if (step+stones[i] == stones[stones.length-1]) return true;
                int dest = step+stones[i];
                if(steps.containsKey(dest))
                {
                    steps.get(dest).add(step);
                    steps.get(dest).add(step+1);
                    if(step - 1 > 0) steps.get(dest).add(step-1);
                }
            }
        }
        return false;
        
    }
}