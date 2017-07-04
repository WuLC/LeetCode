/*
* @Author: WuLC
* @Date:   2017-07-04 15:10:29
* @Last Modified by:   WuLC
* @Last Modified time: 2017-07-04 15:41:24
* @Email: liangchaowu5@gmail.com
*/


// priority queue
public class Solution 
{
    public List<Integer> topKFrequent(int[] nums, int k) 
    {
        Map<Integer, Integer> count = new HashMap<Integer, Integer>();
        for(int num : nums)
        {
            if (!count.containsKey(num)) count.put(num, 0);
            count.put(num, count.get(num)+1);
        }
        
        PriorityQueue<Map.Entry<Integer, Integer>> pq = new PriorityQueue<>(
        new Comparator<Map.Entry<Integer, Integer>>()
            {
                @Override
                public int compare(Map.Entry<Integer, Integer> m1, Map.Entry<Integer, Integer> m2)
                {
                    return m2.getValue() - m1.getValue();
                }
            }
        );
        
        pq.addAll(count.entrySet());
        List<Integer> result = new ArrayList<Integer>();
        for(int i = 0; i < k; i++)
        {
            result.add(pq.poll().getKey());
        }
        return result;
    }
}


// sort the map
public class Solution 
{
    public List<Integer> topKFrequent(int[] nums, int k) 
    {
        Map<Integer, Integer> count = new HashMap<>();
        for(int num : nums)
        {
            if (!count.containsKey(num)) count.put(num, 0);
            count.put(num, count.get(num)+1);
        }
        
        List<Map.Entry<Integer, Integer>> entryList = new ArrayList<Map.Entry<Integer, Integer>>(count.entrySet());
        Collections.sort(entryList, new Comparator<Map.Entry<Integer, Integer>>()
            {
                @Override
                public int compare(Map.Entry<Integer, Integer> m1, Map.Entry<Integer, Integer> m2)
                {
                    return m2.getValue() - m1.getValue();
                }
            }
        );
        
        List<Integer> result = new ArrayList<Integer>();
        for(int i = 0; i < k; i++) result.add(entryList.get(i).getKey());
        return result;
    }
}