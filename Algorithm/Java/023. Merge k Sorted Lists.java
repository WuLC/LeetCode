/**
* Author: LC
* Date:   2016-11-04 09:12:35
* Last modified by:   WuLC
* Last Modified time: 2016-11-04 09:14:37
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


// build the min-heap, get the smallest element each time
// time complexity O(nlogm), n is the number of the nodes, and m is the number of the link-list
public class Solution 
{
    private ListNode[] nodeList;
    private int right;
    
    public ListNode mergeKLists(ListNode[] lists) 
    {
        // remove empry list from the array
        List<ListNode> nodes = new ArrayList<ListNode>();
        for (ListNode node:lists)
            if (node != null) nodes.add(node);
        nodeList = nodes.toArray(new ListNode[nodes.size()]);
        
        right = nodeList.length - 1;
        
        // init the minimum heap
        for (int i=(nodeList.length>>1) - 1; i>=0; i--) siftDown(i);
        
        ListNode dummy = new ListNode(0);
        ListNode curr = dummy;
        // get the current min element
        while (0 <= right)
        {
            if (nodeList[0] != null)
            {
                curr.next = nodeList[0];
                nodeList[0] = nodeList[0].next;
                curr = curr.next;
            }

            if (nodeList[0] == null && right>0)  nodeList[0] = nodeList[right--];
            
            if (nodeList[0] != null) siftDown(0);
            else break;
        }
        return dummy.next;
    }
    
    public void siftDown(int i)
    {
        ListNode tmp;
        while (i < right)
        {
            if ( i*2+2 <= right && nodeList[i*2+2] != null && nodeList[i*2+2].val < nodeList[i].val && nodeList[i*2+2].val < nodeList[i*2+1].val )
            {
                tmp = nodeList[i];
                nodeList[i] = nodeList[i*2+2];
                nodeList[i*2+2] = tmp;
                i = i*2+2;
            }
            else if(i*2+1 <= right && nodeList[i*2+1] != null && nodeList[i*2+1].val < nodeList[i].val)
            {
                tmp = nodeList[i];
                nodeList[i] = nodeList[i*2+1];
                nodeList[i*2+1] = tmp;
                i = i*2+1;
            }
            else break;
        }
    }
}