/*
* @Author: WuLC
* @Date:   2017-05-27 11:21:08
* @Last Modified by:   WuLC
* @Last Modified time: 2017-05-27 11:37:33
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
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

// recursive, O(n) space
public class Solution 
{
    public TreeNode sortedListToBST(ListNode head) 
    {
        List<Integer> vals = new ArrayList<Integer>();
        ListNode curr = head;
        while(curr != null)
        {
            vals.add(curr.val);
            curr = curr.next;
        }
        return dfs(vals, 0, vals.size()-1);
    }
    
    public TreeNode dfs(List<Integer> vals, int start, int end)
    {
        if (start > end) return null;
        int mid = start + ((end - start)>>1);
        TreeNode root = new TreeNode(vals.get(mid));
        root.left = dfs(vals, start, mid-1);
        root.right = dfs(vals, mid + 1, end);
        return root;
    }
}

// recursive, O(1) space 
public class Solution 
{
    public TreeNode sortedListToBST(ListNode head) 
    {
        if (head == null) return null;
        if (head.next == null) return new TreeNode(head.val);
        
        ListNode curr = head;
        int count = 0;
        while (curr != null)
        {
            count ++;
            curr = curr.next;
        }
        
        curr = head;
        for(int i = 0; i < (count>>1)-1; i++) curr = curr.next;
        
        TreeNode root = new TreeNode(curr.next.val);
        root.right = sortedListToBST(curr.next.next);
        curr.next = null;
        root.left = sortedListToBST(head);
        return root;
    }
}

// referer O(1) space solution, the highlight is to traverse the linked once to find the median node
public class Solution 
{
	public TreeNode sortedListToBST(ListNode head) 
	{
	    if(head==null) return null;
	    return toBST(head,null);
	}
	public TreeNode toBST(ListNode head, ListNode tail)
	{
	    ListNode slow = head;
	    ListNode fast = head;
	    if(head==tail) return null;
	    while(fast!=tail&&fast.next!=tail)
	    {
	        fast = fast.next.next;
	        slow = slow.next;
	    }
	    TreeNode thead = new TreeNode(slow.val);
	    thead.left = toBST(head,slow);
	    thead.right = toBST(slow.next,tail);
	    return thead;
	}
}