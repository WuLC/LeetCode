/*
 * Created on Tue Mar 13 2018 22:44:21
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
 // two pointers
public class Solution 
{
    public boolean hasCycle(ListNode head) 
    {
        ListNode p1 = head, p2 = head;
        while (p1 != null && p2 != null && p2.next != null)
        {
            p1 = p1.next;
            p2 = p2.next.next;
            if (p1==p2) return true;
        }
        return false;
    }
}