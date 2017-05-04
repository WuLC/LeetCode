/**
* Author: WuLC
* Date:   2017-05-04 15:57:02
* Last modified by:   WuLC
* Last Modified time: 2017-05-04 15:57:36
* Email: liangchaowu5@gmail.com
*/


/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */

// use four pointers, operate on the list
public class Solution 
{
    public ListNode reverseBetween(ListNode head, int m, int n) 
    {
        if (m==n) return head;
        ListNode p1 = null, p2 = null, p3 = null, tmp = null;
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        p1 = dummy;
        p2 = dummy.next;
        int count = 1;
        while (count < m)
        {
            p1 = p1.next;
            p2 = p2.next;
            count += 1;
        }
        if(p2 != null) p3 = p2.next;
        while (count < n)
        {
            tmp = p3.next;
            p3.next = p2;
            p2 = p3;
            p3 = tmp;
            count += 1;
        }
        p1.next.next = p3;
        p1.next = p2;
        return dummy.next;
    }
}