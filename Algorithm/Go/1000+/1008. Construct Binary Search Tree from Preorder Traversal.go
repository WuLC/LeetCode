/*
 * Created on Tue Mar 12 2019 9:12:39
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
func bstFromPreorder(preorder []int) *TreeNode {
	return dfs(preorder, 0, len(preorder))
}

func dfs(preorder []int, left int, right int) *TreeNode {
	if left == right {
		return nil
	}
	root := &TreeNode{preorder[left], nil, nil}
	r := left + 1
	for r < len(preorder) && preorder[r] < preorder[left] {
		r++
	}
	root.Left = dfs(preorder, left+1, r)
	root.Right = dfs(preorder, r, right)
	return root
}