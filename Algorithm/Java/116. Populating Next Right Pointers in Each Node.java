/**
* Author: WuLC
* Date:   2017-05-18 00:11:45
* Last modified by:   WuLC
* Last Modified time: 2017-05-18 00:12:37
* Email: liangchaowu5@gmail.com
*/


/**
 * Definition for binary tree with next pointer.
 * public class TreeLinkNode {
 *     int val;
 *     TreeLinkNode left, right, next;
 *     TreeLinkNode(int x) { val = x; }
 * }
 */

// O(1) space, modify next pointer for each node level by level
public class Solution 
{
    public void connect(TreeLinkNode root) 
    {
        TreeLinkNode leftMost, curr;
        leftMost = root;
        while (leftMost != null)
        {
            curr = leftMost;
            while (curr != null && curr.left != null)
            {
                curr.left.next = curr.right;
                if (curr.next != null) curr.right.next = curr.next.left;
                curr = curr.next;
            }
            leftMost = leftMost.left;
        }
    }
}