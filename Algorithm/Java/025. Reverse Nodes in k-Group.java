/**
* Author: WuLC
* Date:   2016-10-26 11:34:13
* Last modified by:   WuLC
* Last Modified time: 2016-10-26 12:52:29
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


// method 1, O(n) time ,O(1) space
// use the function reverse to reverse a linked list with specific head and tail
public class Solution 
{
    public ListNode reverseKGroup(ListNode head, int k) 
    {
        if (k<=1 || head == null || head.next == null) return head;
        ListNode dummy = new ListNode(0);
        ListNode curr=dummy, p1=head, p2=head, tmp;
        int count=1;
        while (p2!=null)
        {
            for(int i=0; i<k-1; i++)
            {
                if (p2==null) break;
                p2 = p2.next;
                count += 1;
            }
            if (count == k && p2 != null)
            {
                tmp = p2.next;
                curr.next = reverse(p1, p2);
                curr = p1;
                p1 = p2 = tmp;
                count = 1;
            }
            else
            {
                curr.next = p1;
                break;
            }
        }
        return dummy.next;
    }
    
    // the length of the linked list is assured to be larger than 1
    public ListNode reverse(ListNode head, ListNode tail)
    {
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode p1 = head, p2 = head.next, tmp= null;
        head.next = null;
        while (true)
        {
            tmp = p2.next;
            p2.next = p1;
            if (p2 == tail) break;
            p1 = p2;
            p2 = tmp;
        }
        return tail;
    }
}


// method 2, O(n) time, O(n) space
// recursive, concise code, but a recursive function must occupy at least O(n) stack space, where n is the depth of the recursion.
public ListNode reverseKGroup(ListNode head, int k) {
    ListNode curr = head;
    int count = 0;
    while (curr != null && count != k) { // find the k+1 node
        curr = curr.next;
        count++;
    }
    if (count == k) { // if k+1 node is found
        curr = reverseKGroup(curr, k); // reverse list with k+1 node as head
        // head - head-pointer to direct part, 
        // curr - head-pointer to reversed part;
        while (count-- > 0) { // reverse current k-group: 
            ListNode tmp = head.next; // tmp - next head in direct part
            head.next = curr; // preappending "direct" head to the reversed list 
            curr = head; // move head of reversed part to a new node
            head = tmp; // move "direct" head to the next node in direct part
        }
        head = curr;
    }
    return head;
}