/*
 * Created on Sun Jun 09 2019 18:6:37
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

// simple recursive
func sufficientSubset(root *TreeNode, limit int) *TreeNode {
	if root.Left == nil && root.Right == nil {
		if root.Val < limit {
			return nil
		} else {
			return root
		}
	}
	if root.Left != nil {
		root.Left = sufficientSubset(root.Left, limit - root.Val)
	} 
	if root.Right != nil {
		root.Right = sufficientSubset(root.Right, limit - root.Val)
	}
	if root.Left != nil || root.Right != nil {
		return root
	} else {
		return nil
	}
}