/**
* Author: WuLC
* Date:   2017-05-24 09:37:28
* Last modified by:   WuLC
* Last Modified time: 2017-05-24 09:44:38
* Email: liangchaowu5@gmail.com
*/

/**
 * Definition for singly-linked list with a random pointer.
 * class RandomListNode {
 *     int label;
 *     RandomListNode next, random;
 *     RandomListNode(int x) { this.label = x; }
 * };
 */

// hashmap
// traverse the linked twice,  deal with next pointer the first time and random pointer for the second time 
public class Solution 
{
    public RandomListNode copyRandomList(RandomListNode head) 
    {
        RandomListNode dummy, copy_curr;
        dummy = new RandomListNode(0);
        copy_curr = dummy;
        RandomListNode curr = head;
        Map<RandomListNode, RandomListNode> mapping = new HashMap<RandomListNode, RandomListNode>();
        
        while (curr != null)
        {
            copy_curr.next = new RandomListNode(curr.label);
            copy_curr = copy_curr.next;
            mapping.put(curr, copy_curr);
            curr = curr.next;
        }
        
        curr = head;
        copy_curr = dummy.next;
        while(curr != null)
        {
            copy_curr.random = mapping.get(curr.random);
            curr = curr.next;
            copy_curr = copy_curr.next;
        }
        return dummy.next;
    }
}