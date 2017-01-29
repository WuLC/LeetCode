/**
* Author: WuLC
* Date:   2017-01-29 20:55:27
* Last modified by:   WuLC
* Last Modified time: 2017-01-29 20:56:05
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

// two pointers, delete duplicate nodes from the original list
public class Solution 
{
    public ListNode deleteDuplicates(ListNode head) 
    {
        if(head == null) return head;
        ListNode p1 = head, p2 = head.next;
        while(p2 != null)
        {
            if(p1.val != p2.val)
            {
                p1 = p1.next;
                p1.val = p2.val;
            }
            p2 = p2.next;
        }
        p1.next = null;
        return head;
    }
}