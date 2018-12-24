/*
 * Created on Mon Dec 24 2018 19:36:3
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

// stack, O(n) time
// define custom stack type
package main

type Stack struct {
	nums []int
}

func (s *Stack) Peak() int {
	return s.nums[len(s.nums)-1]
}

func (s *Stack) Push(val int) {
	s.nums = append(s.nums, val)
}

func (s *Stack) Pop() int {
	val := s.nums[len(s.nums)-1]
	s.nums = s.nums[:len(s.nums)-1]
	return val
}

func (s *Stack) Size() int {
	return len(s.nums)
}

func maxWidthRamp(A []int) int {
	s := &Stack{[]int{0}}
	for i := 1; i < len(A); i++ {
		if A[i] < A[s.Peak()] {
			s.Push(i)
		}
	}
	result := 0
	for i := len(A) - 1; i >= 0; i-- {
		for s.Size() > 0 && A[i] >= A[s.Peak()] {
			val := s.Pop()
			if result < (i - val) {
				result = i - val
			}
		}
		if s.Size() == 0 {
			break
		}
	}
	return result
}
