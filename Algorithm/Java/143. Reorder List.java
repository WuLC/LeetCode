/*
 * Created on Sat Feb 10 2018 22:57:42
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

// recursive
class Solution 
{
    public void reorderList(ListNode head) 
    {
        helper(head);
    }

    private ListNode helper(ListNode head)
    {
        if (head == null || head.next == null || head.next.next == null)
            return head;
        ListNode curr = head;
        while (curr.next.next != null) curr = curr.next;
        ListNode nextLevel = head.next;
        head.next = curr.next;
        curr.next = null;
        head.next.next = helper(nextLevel);
        return head;
    }
}