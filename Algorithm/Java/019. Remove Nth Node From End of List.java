/**
* Author: WuLC
* Date:   2016-10-25 15:05:24
* Last modified by:   WuLC
* Last Modified time: 2016-10-25 15:05:59
* Email: liangchaowu5@gmail.com
*/

/**
 * Definition for singly-linked list.
 * public class ListNode 
 * {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */


// two pointers with dummy node
public class Solution 
{
    public ListNode removeNthFromEnd(ListNode head, int n) 
    {
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode p1 = dummy, p2 = dummy;
        for (int i=0; i < n; i++)
            p2 = p2.next;
        while (p2.next != null)
        {
            p1 = p1.next;
            p2 = p2.next;
        }
        p1.next = p1.next.next;
        return dummy.next;
    }
}