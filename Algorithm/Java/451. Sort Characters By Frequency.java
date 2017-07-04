/*
* @Author: WuLC
* @Date:   2017-07-04 14:55:50
* @Last Modified by:   WuLC
* @Last Modified time: 2017-07-04 14:56:23
* @Email: liangchaowu5@gmail.com
*/

// priority queue
public class Solution 
{
    public String frequencySort(String s) 
    {
        Map<Character, Integer> count = new HashMap<Character, Integer>();
        for (char c : s.toCharArray())
        {
            if (!count.containsKey(c)) count.put(c, 0);
            count.put(c, count.get(c)+1);
        }
        
        PriorityQueue<Map.Entry<Character, Integer>> pq = new PriorityQueue<Map.Entry<Character, Integer>>(
            new Comparator<Map.Entry<Character, Integer>>()
            {
                @Override
                public int compare(Map.Entry<Character, Integer> m1, Map.Entry<Character, Integer> m2)
                {
                    return m2.getValue() - m1.getValue();
                }
            }
        );
        
        pq.addAll(count.entrySet());
        String result = "";
        Map.Entry<Character, Integer> tmp;
        while(pq.size() > 0)
        {
            tmp = pq.poll();
            result += new String(new char[tmp.getValue()]).replace("\0", String.valueOf(tmp.getKey()));
        }
        return result;
    }
}