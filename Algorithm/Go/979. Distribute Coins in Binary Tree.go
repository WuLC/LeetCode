/*
 * Created on Fri Jan 25 2019 9:17:36
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

 // recursive with postorder traverse
func distributeCoins(root *TreeNode) int {
	result := 0
	traverse(root, &result)
	return result
}

func traverse(root *TreeNode, result *int) int {
    if root == nil {
		return 0
	}
	left, right := traverse(root.Left, result), traverse(root.Right, result)
	*result += abs(left) + abs(right)
	return root.Val + left + right - 1
}

func abs(val int) int {
	if val < 0 {
		return -1*val
	} else {
		return val
	}
}