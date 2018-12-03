/*
 * Created on Mon Dec 03 2018 9:3:16
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
func flipEquiv(root1 *TreeNode, root2 *TreeNode) bool {
	if root1 == nil && root2 == nil {
		return true
	} else if root1 == nil || root2 == nil {
		return false
	} else {
		return root1.Val == root2.Val &&
			((flipEquiv(root1.Left, root2.Left) && flipEquiv(root1.Right, root2.Right)) ||
				(flipEquiv(root1.Left, root2.Right) && flipEquiv(root1.Right, root2.Left)))
	}
}