/*
* @Author: LC
* @Date:   2017-08-28 23:56:28
* @Last Modified by:   LC
* @Last Modified time: 2017-08-28 23:56:48
*/


/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */

// two pointers
class Solution 
{
    public ListNode oddEvenList(ListNode head) 
    {
        if (head == null || head.next == null) return head;
        ListNode p1 = head, p2 = head.next, head2 = head.next;
        while(p1.next != null && p2.next != null)
        {
            p1.next = p2.next;
            p1 = p1.next;
            p2.next = p1.next;
            p2 = p2.next;
        }
        p1.next = head2;
        return head;
    }
}