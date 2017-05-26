/*
* @Author: WuLC
* @Date:   2017-05-26 20:13:59
* @Last Modified by:   WuLC
* @Last Modified time: 2017-05-26 20:14:37
* @Email: liangchaowu5@gmail.com
*/

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */


// store duplicate numbers in a set
// O(n) time, O(n) space
public class Solution 
{
    public ListNode deleteDuplicates(ListNode head) 
    { 
        if  (head == null || head.next == null) return head;
    
        // find duplicate elements
        ListNode curr = head;
        Set<Integer> duplicate = new HashSet<Integer>();
        while ( curr.next != null)
        {
            if (curr.val == curr.next.val) duplicate.add(curr.val);
            curr = curr.next;
        }
        
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode p1 = dummy;
        curr = head;
        while (curr != null)
        {
            if (!duplicate.contains(curr.val))
            {
                p1.next = curr;
                p1 = p1.next;
            }
            curr = curr.next;
        }
        p1.next = null;
        return dummy.next;
    }
}