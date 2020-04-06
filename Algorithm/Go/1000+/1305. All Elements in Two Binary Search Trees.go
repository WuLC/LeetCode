/*
 * Created on Sun Jan 18 2020 10:21:10
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

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */



 func reachLeftMost(root *TreeNode, stack *[]*TreeNode) *TreeNode {
    for root != nil && root.Left != nil {
        *stack = append(*stack, root)
        root = root.Left
    }
    return root
}

func getAllElements(root1 *TreeNode, root2 *TreeNode) []int {
    s1, s2 := []*TreeNode{}, []*TreeNode{}
    n1, n2 := reachLeftMost(root1, &s1), reachLeftMost(root2, &s2)
    result := []int{}
    for (n1 != nil || len(s1) > 0) || (n2 != nil || len(s2) > 0) {
        if n1 == nil && len(s1) > 0 {
            n1 = s1[len(s1)-1]
            s1 = s1[:len(s1)-1]
            
        }
        if n2 == nil && len(s2) > 0 {
            n2 = s2[len(s2)-1]
            s2 = s2[:len(s2)-1]
        }

        if (n1 != nil && n2 != nil && n1.Val < n2.Val) || (n2 == nil) {
                result = append(result, n1.Val)
                n1 = reachLeftMost(n1.Right, &s1)
            } else {
                result = append(result, n2.Val)
                n2 = reachLeftMost(n2.Right, &s2)
            }
    }
    return result
}