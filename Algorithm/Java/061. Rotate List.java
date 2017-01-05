/**
* Author: WuLC
* Date:   2017-01-05 20:24:55
* Last modified by:   WuLC
* Last Modified time: 2017-01-05 20:34:22
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


// 
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */

// simplify k so that  k < length of the list, then use two pointers to traverse the list 
public class Solution 
{
    public ListNode rotateRight(ListNode head, int k) 
    {
        // simpify k
        ListNode curr = head;
        int length = 0;
        while (curr != null)
        {
            length += 1;
            curr =curr.next;
        }
        if (length == 0 || k%length == 0) return head;
        k %= length;
        
    
        ListNode p1 = head, p2 = head;
        for(int i=0; i<k; i++) p2 = p2.next;
        
        while (p2.next != null)
        {
            p1 = p1.next;
            p2 = p2.next;
        }
        p2.next = head;
        head = p1.next;
        p1.next = null;
        return head;
    }
}