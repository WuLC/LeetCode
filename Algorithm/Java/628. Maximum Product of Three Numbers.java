/*
 * Created on Tue Mar 27 2018 20:40:57
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

// use heap to store largest numbers and smallest numbers
class Solution 
{
    public int maximumProduct(int[] nums) 
    {
        PriorityQueue<Integer> maxNums = new PriorityQueue<Integer>(3);
        PriorityQueue<Integer> minNums = new PriorityQueue<Integer>(2);
        for (int num:nums)
        {
            if (maxNums.size() < 3) maxNums.add(num);
            else if(maxNums.peek() < num)
            {
                maxNums.poll();
                maxNums.add(num);
            }
            if (minNums.size() < 2) minNums.add(-num);
            else if(minNums.peek() < -num)
            {
                minNums.poll();
                minNums.add(-num);
            }
        }
        ArrayList<Integer> largest = new ArrayList<Integer>();
        ArrayList<Integer> smallest = new ArrayList<Integer>();
        while (maxNums.size() != 0) largest.add(maxNums.poll());
        while (minNums.size() != 0) smallest.add(-minNums.poll());
        return Math.max(largest.get(0)*largest.get(1)*largest.get(2), largest.get(2)*smallest.get(0)*smallest.get(1));
    }
}