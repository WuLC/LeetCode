/*
* @Author: WuLC
* @Date:   2017-07-01 17:39:55
* @Last Modified by:   WuLC
* @Last Modified time: 2017-07-01 17:40:31
* @Email: liangchaowu5@gmail.com
*/


// hashmap
public class Solution 
{
    public int[] intersect(int[] nums1, int[] nums2) 
    {
        Map<Integer, Integer> count1 = new HashMap<Integer, Integer>();
        for(int num : nums1)
        {
            if (!count1.containsKey(num)) count1.put(num, 0);
            count1.put(num, count1.get(num)+1);
        }
        
        List<Integer> intersect = new ArrayList<Integer>();
        for(int num : nums2)
        {
            if (count1.containsKey(num))
            {
                intersect.add(num);
                count1.put(num, count1.get(num)-1);
                if(count1.get(num) == 0) count1.remove(num);
            }
        }
        
        int[] result = new int[intersect.size()];
        int i = 0;
        for(int num:intersect) result[i++] = num;
        return result;
    }
}