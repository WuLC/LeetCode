/*
* @Author: WuLC
* @Date:   2017-05-28 14:22:10
* @Last Modified by:   WuLC
* @Last Modified time: 2017-05-28 14:23:15
* @Email: liangchaowu5@gmail.com
*/

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */


// Reservoir Sampling
// referer: https://discuss.leetcode.com/topic/53753/brief-explanation-for-reservoir-sampling
public class Solution {

    private ListNode dummy = new ListNode(0);
    
    public Solution(ListNode head) 
    {
        dummy.next = head;
    }
    
    
    public int getRandom()
    {
        ListNode curr = dummy.next;
        int count = 0, result = 0;
        while (curr != null)
        {
            count ++;
            if (Math.random() < 1.0/count) result = curr.val;
            curr = curr.next;
        }
        return result;
    }
}