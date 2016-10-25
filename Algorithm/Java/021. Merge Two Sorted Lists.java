/**
* Author: WuLC
* Date:   2016-10-25 21:45:32
* Last modified by:   WuLC
* Last Modified time: 2016-10-25 21:46:03
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

public class Solution 
{
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) 
    {
        ListNode dummy = new ListNode(0);
        ListNode curr = dummy;
        
        while (l1 != null || l2!=null)
        {
            if (l1 == null)
            {
                curr.next = l2;
                break;
            }
            if (l2 == null)
            {
                curr.next = l1;
                break;
            }
            if (l1.val < l2.val)
            {
                curr.next = l1;
                l1 = l1.next;
                curr = curr.next;
            }
            else
            {
                curr.next = l2;
                l2 = l2.next;
                curr = curr.next;
            }
        }
        return dummy.next;
    }
}