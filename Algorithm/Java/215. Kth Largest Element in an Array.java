/*
 * Created on Tue Mar 27 2018 17:2:3
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

// priority queue
class Solution 
{
    public int findKthLargest(int[] nums, int k) 
    {
        PriorityQueue<Integer> largestK = new PriorityQueue<Integer>(k);
        for(int num : nums)
        {
            if (largestK.size() < k) largestK.add(num);
            else if (largestK.peek() < num)
            {
                largestK.poll();
                largestK.add(num);
            }
        }
        return largestK.peek();
    }
}