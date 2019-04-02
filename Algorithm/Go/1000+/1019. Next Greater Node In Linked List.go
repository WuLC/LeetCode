/*
 * Created on Tue Apr 02 2019 11:59:56
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

// stack, O(n) time, O(n) space
func nextLargerNodes(head *ListNode) []int {
	result, stack := []int{}, [][]int{}
	count, p := 0, head
	for p != nil {
		result = append(result, 0)
		for len(stack) > 0 && stack[len(stack)-1][1] < p.Val {
			result[stack[len(stack)-1][0]] = p.Val
			stack = stack[:len(stack)-1]
		}
		stack = append(stack, []int{count, p.Val})
		count++
		p = p.Next
	}
	return result
}