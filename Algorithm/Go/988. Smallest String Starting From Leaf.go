/*
 * Created on Sun Feb 03 2019 18:41:25
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

// recursive
import "strings"

func smallestFromLeaf(root *TreeNode) string {
    if root == nil {
		return ""
	}
	left, right := smallestFromLeaf(root.Left), smallestFromLeaf(root.Right)
	if len(left) == 0 {
		return right + string(root.Val + 97)
	} else if len(right) == 0  {
		return left + string(root.Val + 97)
	} else {
		return min(left, right) + string(root.Val + 97) 
	}
}

func min(s1, s2 string) string {
	if strings.Compare(s1, s2) < 0 {
		return s1
	} else {
		return s2
	}
}