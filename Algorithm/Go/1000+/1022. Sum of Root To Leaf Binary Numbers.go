/*
 * Created on Tue Apr 09 2019 10:31:19
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

func sumRootToLeaf(root *TreeNode) int {
	return dfs(root, 0)
}

func dfs(root *TreeNode, curr int) int {
	if root.Left == nil && root.Right == nil {
		return curr*2 + root.Val
	}
	tmp := 0
	if root.Left != nil {
		tmp += dfs(root.Left, curr * 2 + root.Val)
	}
	if root.Right != nil {
		tmp += dfs(root.Right, curr * 2 + root.Val)
	}
	return tmp
}

