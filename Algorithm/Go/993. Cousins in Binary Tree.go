/*
 * Created on Mon Feb 18 2019 9:8:33
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

func isCousins(root *TreeNode, x int, y int) bool {
	if root.Val == x || root.Val == y {
		return false
	}
	record := []int{}
	dfs(root, &record, x, y, 0)
	return record[0] != record[2] && record[1] == record[3]
}

func dfs(root *TreeNode, record *[]int, x, y, depth int) {
	if len(*record) == 4 {
		return
	}
	if root.Left != nil {
		if root.Left.Val == x || root.Left.Val == y {
			*record = append(*record, root.Val)
			*record = append(*record, depth+1)
		}
		dfs(root.Left, record, x, y, depth+1)
	}
	if root.Right != nil {
		if root.Right.Val == x || root.Right.Val == y {
			*record = append(*record, root.Val)
			*record = append(*record, depth+1)
		}
		dfs(root.Right, record, x, y, depth+1)
	}
}