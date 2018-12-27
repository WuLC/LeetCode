/*
 * Created on Thu Dec 27 2018 14:52:57
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

// stack, O(n) time
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

func sumSubarrayMins(A []int) int {
	n := len(A)
	left, s := []int{}, &Stack{[]int{}}
	for i := 0; i < n; i++ {
		for s.Size() > 0 && A[s.Peak()] >= A[i] {
			s.Pop()
		}
		if s.Size() > 0 {
			left = append(left, i-s.Peak())
		} else {
			left = append(left, i+1)
		}
		s.Push(i)
	}

	right, rs := []int{}, &Stack{[]int{}}
	for i := n - 1; i >= 0; i-- {
		for rs.Size() > 0 && A[rs.Peak()] > A[i] {
			rs.Pop()
		}
		if rs.Size() > 0 {
			right = append(right, rs.Peak()-i)
		} else {
			right = append(right, n-i)
		}
		rs.Push(i)
	}

	result := 0
	MOD := 1000000007
	for i := 0; i < n; i++ {
		result += (A[i] * left[i] * right[n-i-1]) % MOD
		result %= MOD
	}
	return result
}