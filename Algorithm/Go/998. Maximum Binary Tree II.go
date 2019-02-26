/*
 * Created on Tue Feb 26 2019 21:27:6
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

// recursive, always insert to the right subtree of the current root
func insertIntoMaxTree(root *TreeNode, val int) *TreeNode {
	if root == nil || root.Val < val {
		new_root := new(TreeNode)
		new_root.Val = val
		new_root.Left = root
		return new_root
	} else {
		root.Right = insertIntoMaxTree(root.Right, val)
		return root
	}
}