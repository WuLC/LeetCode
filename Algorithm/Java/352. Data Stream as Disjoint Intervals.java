/**
* Author: WuLC
* Date:   2017-04-20 14:58:29
* Last modified by:   WuLC
* Last Modified time: 2017-04-20 15:00:35
* Email: liangchaowu5@gmail.com
*/

// use TreeMap in Java, O(logn) time complexity
// referer: https://discuss.leetcode.com/topic/46887/java-solution-using-treemap-real-o-logn-per-adding


/**
 * Definition for an interval.
 * public class Interval {
 *     int start;
 *     int end;
 *     Interval() { start = 0; end = 0; }
 *     Interval(int s, int e) { start = s; end = e; }
 * }
 */
 
public class SummaryRanges 
{
    private TreeMap<Integer, Interval> tree;
 
    public SummaryRanges() 
    {
        tree = new TreeMap<Integer, Interval>();
    }
    
    
    public void addNum(int val) 
    {
        if (tree.containsKey(val)) return;
        Integer lower = tree.lowerKey(val);  // must use Integer, cause there may be null type
        Integer higher = tree.higherKey(val);
        if (lower != null && higher != null && tree.get(lower).end + 1 == val && tree.get(higher).start == val + 1)
        {
            tree.get(lower).end = tree.get(higher).end;
            tree.remove(higher);
        }
        else if(higher != null && tree.get(higher).start == val + 1)
        {
            // can not modify start of interval directly, cause key is related to it
            tree.put(val, new Interval(val, tree.get(higher).end));
            tree.remove(higher);
        }
        else if(lower != null && tree.get(lower).end + 1 >= val)
        {
            tree.get(lower).end = Math.max(val, tree.get(lower).end);
        }
        else
        {
            tree.put(val, new Interval(val, val));
        }
    }
    
    
    public List<Interval> getIntervals() 
    {
        return new ArrayList<Interval>(tree.values());
    }
}
