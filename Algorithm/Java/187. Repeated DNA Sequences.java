/**
* Author: LC
* Date:   2017-06-07 13:14:25
* Last modified by:   WuLC
* Last Modified time: 2017-06-07 13:14:44
* Email: liangchaowu5@gmail.com
*/


// hash table
public class Solution 
{
    public List<String> findRepeatedDnaSequences(String s) 
    {
        List<String> result = new ArrayList<String>();
        Map<String, Integer> count = new HashMap<String, Integer>();
        for(int i = 0; i <= s.length() - 10; i++)
        {
            String tmp = s.substring(i, i+10);
            if (count.containsKey(tmp)) count.put(tmp, count.get(tmp) + 1);
            else count.put(tmp, 1);
        }
        for(Map.Entry<String, Integer> entry : count.entrySet())
        {
            if (entry.getValue() > 1) result.add(entry.getKey());
        }
        return result;
    }
}