/*
* @Author: WuLC
* @Date:   2017-07-31 13:07:54
* @Last Modified by:   WuLC
* @Last Modified time: 2017-07-31 13:08:37
* @Email: liangchaowu5@gmail.com
*/

// dfs
public class Solution 
{
    private List<Integer> hours;
    private List<Integer> miniutes;
    public List<String> readBinaryWatch(int num) 
    {
        List<String> result = new ArrayList<String>();
        for (int i = 0; i < 4; i++)
        {
            hours = new ArrayList<Integer>();
            miniutes = new ArrayList<Integer>();
            getHour(i, 0, 0);
            getMiniute(num - i, 0, 0);
            String miniute;
            int h, m;
            for(int j = 0; j < hours.size(); j++)
            {
                for(int k = 0; k < miniutes.size(); k++)
                {
                    h = hours.get(j);
                    m = miniutes.get(k);
                    if(m < 10) result.add(String.valueOf(h)+":0"+String.valueOf(m));
                    else result.add(String.valueOf(h)+":"+String.valueOf(m));
                }    
            }
        }
        return result;
    }
    
    public void getHour(int n, int idx, int val)
    {
        if (n == 0 && val <= 11)
        {
            hours.add(val);
            return;
        }
        for(int i = idx; i < 4 ;i++)
            if ((val ^ (1 << idx)) <= 11) 
                getHour(n - 1, i + 1, val ^ (1 << i));
    }
    
    public void getMiniute(int n, int idx, int val)
    {
        if (n == 0 && val <= 59)
        {
            miniutes.add(val);
            return;
        }
        for(int i = idx; i < 6 ;i++)
            if ((val ^ (1 << idx)) <= 59) 
                getMiniute(n - 1, i + 1, val ^ (1 << i));
        
    }
}