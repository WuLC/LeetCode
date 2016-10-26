/**
* Author: WuLC
* Date:   2016-10-26 13:11:42
* Last modified by:   WuLC
* Last Modified time: 2016-10-26 13:12:48
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

// O(n) time, O(1) space
public class Solution 
{
    public ListNode swapPairs(ListNode head) 
    {
        if (head == null || head.next == null) return head;
        
        ListNode dummy = new ListNode(0);
        ListNode curr = dummy, p1 = head, p2 = head.next, tmp;
        while (p2!=null)
        {
            tmp = p2.next;
            p2.next = p1;
            curr.next = p2;
            curr = p1;
            p1 = tmp;
            if (tmp == null) break;
            p2 = tmp.next;
        }
        curr.next = p1;
        return dummy.next;
    }
}