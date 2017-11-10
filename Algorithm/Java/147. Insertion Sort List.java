/*
 * Created on Fri Nov 10 2017 14:28:16
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

// Insertion sort
// O(n^2) time, O(1) space


/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution 
{
    public ListNode insertionSortList(ListNode head) 
    {
        if (head == null || head.next == null) return head;
        ListNode curr = head.next, p;
        while(curr != null)
        {
            p = head;
            int tmp = curr.val;
            while(p != curr)
            {
                if (tmp <= p.val)
                {
                    int t = p.val;
                    p.val = tmp;
                    tmp = t;
                }
                p = p.next;
            }
            p.val = tmp;
            curr = curr.next;
        }
        return head;
    }
}
