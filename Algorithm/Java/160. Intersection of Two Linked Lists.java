/**
* Author: WuLC
* Date:   2017-04-17 00:04:35
* Last modified by:   WuLC
* Last Modified time: 2017-04-17 00:09:21
* Email: liangchaowu5@gmail.com
*/


/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */


// traverse the two link lists alternately
// when they have intersection, they should meet after walking same number of steps

public class Solution 
{
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) 
    {
        if (headA == null || headB == null) return null;
        ListNode pa = headA, pb = headB;
        boolean moveA = false, moveB = false;
        while (pa != null || pb != null)
        {
            if (pa == pb) return pa;
            if (pa == null && moveA == false)
            {
                pa = headB;
                moveA = true;
            }
            else if (pa != null) pa = pa.next;
            
            if (pb == null && moveB == false)
            {
                pb = headA;
                moveB = true;
            }
            else if (pb != null) pb = pb.next;
        }
        return null;
    }
}

