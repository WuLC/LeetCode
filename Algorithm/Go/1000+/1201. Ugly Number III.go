func nthUglyNumber(n int, a int, b int, c int) int {
	ab, bc, ac := a*b/gcd(a, b), a*c/gcd(a, c), b*c/gcd(b, c)
	abc := ab * c / gcd(ab, c)
	left, right := 1, n*min(min(a, b), c)
	for left < right {
		mid := left + ((right - left) >> 1)
		k := mid/a + mid/b + mid/c - mid/ab - mid/bc - mid/ac + mid/abc
		if k < n {
			left = mid + 1
		} else {
			right = mid
		}
	}
	return left
}

func gcd(a, b int) int {
	if a < b {
		a, b = b, a
	}
	for b > 0 {
		a, b = b, a%b
	}
	return a
}

func min(a, b int) int {
	if a < b {
		return a
	} else {
		return b
	}
}