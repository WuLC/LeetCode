/*
 * Created on Mon Apr 15 2019 13:5:47
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


// stack, two pointers

import "strconv"
func recoverFromPreorder(S string) *TreeNode {
	p1, p2 := 0, 0
	stack := []*TreeNode{}
	s := []rune(S)
	for p2 < len(s) {
		level := 0
		for s[p1] == '-' {
			p1++
			p2++
			level++
		}
		for p2 < len(s) && s[p2] != '-' {
			p2++
		}
		num, err := strconv.Atoi(string(s[p1 : p2]))
		if err != nil {
			return nil
		}
        curr_node :=  &TreeNode{num, nil, nil}
		if len(stack) > level {
			stack = stack[:level]
		}
		if len(stack) > 0 {
			if stack[level - 1].Left == nil {
				stack[level - 1].Left = curr_node
			} else {
				stack[level - 1].Right = curr_node
			}
		}
		stack = append(stack, curr_node)
		p1 = p2
	}
	return stack[0]
}