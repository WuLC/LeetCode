/*
 * Created on Fri Jan 11 2019 20:49:28
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

// concise dfs
// referer: https://leetcode.com/problems/flip-binary-tree-to-match-preorder-traversal/discuss/214216/JavaC++Python-DFS-Solution
type State struct {
	Result []int
	Idx    int
}

func flipMatchVoyage(root *TreeNode, voyage []int) []int {
	s := State{[]int{}, 0}
	if dfs(root, voyage, &s) {
		return s.Result
	} else {
		return []int{-1}
	}
}

func dfs(root *TreeNode, voyage []int, s *State) bool {
	if root == nil {
		return true
	}
	if root.Val != voyage[s.Idx] {
		return false
	}
	s.Idx += 1
	if root.Left != nil && root.Left.Val != voyage[s.Idx] {
		s.Result = append(s.Result, root.Val)
		return dfs(root.Right, voyage, s) && dfs(root.Left, voyage, s)
	} else {
		return dfs(root.Left, voyage, s) && dfs(root.Right, voyage, s)
	}
}