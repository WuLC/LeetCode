/**
* Author: LC
* Date:   2016-10-10 17:09:41
* Last modified by:   WuLC
* Last Modified time: 2016-10-10 18:04:39
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


// operate directly on the linked list
// notice that, get the number of a single linked list will overflow somttimes
public class Solution 
{
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) 
    {
        ListNode dummy = new ListNode(0);
        ListNode curr = dummy;
        int remainder, carry=0, sum;
        while (l1!=null && l2!=null)
        {
            sum = l1.val + l2.val + carry;
            carry = sum / 10;
            remainder = sum % 10;
            curr.next = new ListNode(remainder);
            curr = curr.next;
            l1 = l1.next;
            l2 = l2.next;
        }
        ListNode tmp = null;
        if (l1!=null) 
            tmp = l1;
        else if (l2!=null)
            tmp = l2;
        while (tmp!=null)
        {
            sum = tmp.val + carry;
            carry = sum / 10;
            remainder = sum % 10;
            curr.next = new ListNode(remainder);
            curr = curr.next;
            tmp = tmp.next;
        }
        if (carry == 1) 
            curr.next= new ListNode(1);
        return dummy.next;
        
    }
}


