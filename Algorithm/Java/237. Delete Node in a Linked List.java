/**
* Author: LC
* Date:   2017-06-13 22:29:38
* Last modified by:   LC
* Last Modified time: 2017-06-13 22:30:42
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

// assign the value of next node to the current one
public class Solution 
{
    public void deleteNode(ListNode node) 
    {
        while ( node.next.next != null )
        {
            node.val = node.next.val;
            node = node.next;
        }
        node.val = node.next.val;
        node.next = null;
    }
}