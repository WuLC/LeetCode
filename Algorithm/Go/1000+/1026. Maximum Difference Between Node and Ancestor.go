/*
 * Created on Sun Apr 14 2019 15:30:3
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

// bottom up dfs
func maxAncestorDiff(root *TreeNode) int {
    return dfs(root)[2]
}


func dfs(root *TreeNode) []int {
	min_num, max_num, max_diff := root.Val, root.Val, 0
	if root.Left != nil {
		left := dfs(root.Left)
		min_num = min(min_num, left[0])
		max_num = max(max_num, left[1])
		max_diff = max(max_diff, left[2])
	}
	if root.Right != nil {
        right := dfs(root.Right)
		min_num = min(min_num, right[0])
		max_num = max(max_num, right[1])
		max_diff = max(max_diff, right[2])
	}
	max_diff = max(max_diff, max(abs(max_num - root.Val), abs(min_num - root.Val)))
	return []int{min_num, max_num, max_diff}
}


func max(a, b int) int {
	if a > b {
		return a
	} else {
		return b
	}
}


func min(a, b int) int {
	if a < b {
		return a
	} else {
		return b
	}
}


func abs(a int) int {
	if a < 0 {
		return a * -1
	} else {
		return a
	}
}