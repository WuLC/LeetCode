/**
* Author: WuLC
* Date:   2017-03-12 23:58:09
* Last modified by:   WuLC
* Last Modified time: 2017-03-12 23:58:56
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


// O(n) space, store smaller values and largers values in two seperate list
public class Solution 
{
    public ListNode partition(ListNode head, int x) 
    {
        List<Integer> smaller = new ArrayList<Integer>();
        List<Integer> larger = new ArrayList<Integer>();
        ListNode curr = head;
        while (curr != null)
        {
            if (curr.val < x) smaller.add(curr.val);
            else larger.add(curr.val);
            curr = curr.next;
        }
        
        curr = head;
        for(int tmp : smaller)
        {
            curr.val = tmp;
            curr = curr.next;
        }
        for(int tmp : larger)
        {
            curr.val = tmp;
            curr = curr.next;
        }
        return head;
    }
}