/*
 * Created on Thu Jan 03 2019 9:44:29
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
func isUnivalTree(root *TreeNode) bool {
	if root.Left != nil {
		same_left := root.Val == root.Left.Val && isUnivalTree(root.Left)
		if !same_left {
			return false
		}
	}
	if root.Right != nil {
		same_right := root.Val == root.Right.Val && isUnivalTree(root.Right)
		if !same_right {
			return false
		}
	}
	return true
}