/*
 * Created on Sun Apr 08 2018 18:28:56
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */


// use two queues, greedy
// pay attention that Queue is a interface in Java, so initialize it with LinkedList
class Solution 
{
    public String predictPartyVictory(String senate) 
    {
        Queue<Integer> rq = new LinkedList<Integer>();
        Queue<Integer> dq = new LinkedList<Integer>();
        char[] cs = senate.toCharArray();
        for(int i=0; i<cs.length; i++)
        {
            if (cs[i] == 'R') rq.offer(i);
            else dq.offer(i);
        }
        int n = cs.length;
        while(dq.size() > 0 && rq.size() > 0)
        {
            if (dq.peek() < rq.peek())
            {
                rq.poll();
                dq.offer(dq.poll() + n);
            }
            else
            {
                dq.poll();
                rq.offer(rq.poll() + n);
            }
        }
        if (dq.size() > 0) return "Dire";
        else return "Radiant";
    }
}