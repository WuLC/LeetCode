/**
* Author: LC
* Date:   2016-10-10 17:09:41
* Last modified by:   WuLC
* Last Modified time: 2016-10-10 18:11:43
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
// notice that  get the number of a single linked list will overflow in some cases
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


// add two number directly, overflow in some test cases
public class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) 
    {
        String num1="", num2 = "";
        while (l1!=null)
        {
            num1 += String.valueOf(l1.val);
            l1 = l1.next;
        }
        while (l2!=null)
        {
            num2 += String.valueOf(l2.val);
            l2 = l2.next;
        }
        long sum = Long.parseLong(new StringBuilder(num1).reverse().toString()) + 
                  Long.parseLong(new StringBuilder(num2).reverse().toString());
        String str = String.valueOf(sum);
        ListNode dummy = new ListNode(0);
        ListNode curr = dummy;
        for (int i = str.length()-1; i>=0; i--)
        {
            curr.next = new ListNode(str.charAt(i) - '0');
            curr = curr.next;
        }
        return dummy.next;
    }
}