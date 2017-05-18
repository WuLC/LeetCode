/*
* @Author: WuLC
* @Date:   2017-05-18 12:33:31
* @Last Modified by:   WuLC
* @Last Modified time: 2017-05-18 12:36:05
* @Email: liangchaowu5@gmail.com
*/

/**
 * Definition for binary tree with next pointer.
 * public class TreeLinkNode {
 *     int val;
 *     TreeLinkNode left, right, next;
 *     TreeLinkNode(int x) { val = x; }
 * }
 */


// similar to problem 116
// just need to traverse layer by layer and record the head node of each row

public class Solution 
{
    public void connect(TreeLinkNode root) 
    {
        TreeLinkNode leftMost, nextLeftMost, curr, tail;
        leftMost = root;
        while (leftMost != null)
        {
            nextLeftMost = null;
            tail = null;
            curr = leftMost;
            while (curr != null)
            {
                if (curr.left != null)
                {
                    if(nextLeftMost == null) 
                    {
                        nextLeftMost = curr.left;
                        tail =  curr.left;
                    }
                    else
                    {
                        tail.next = curr.left;
                        tail = tail.next;
                    }
                }
                if (curr.right != null)
                {
                    if(nextLeftMost == null) 
                    {
                        nextLeftMost = curr.right;
                        tail =  curr.right;
                    }
                    else
                    {
                        tail.next = curr.right;
                        tail = tail.next;
                    }
                }
                curr = curr.next;
            }
            // move to next layer
            leftMost = nextLeftMost;
        }
    }
}