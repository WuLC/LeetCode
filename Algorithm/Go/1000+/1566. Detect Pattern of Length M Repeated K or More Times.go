func containsPattern(arr []int, m int, k int) bool {
	for i := 0; i < len(arr)-m*k+1; i++ {
		for j := 0; j < k; j++ {
			if !equal(arr[i:i+m], arr[i+m*j:i+m*j+m]) {
				break
			}
			if j == k-1 {
				return true
			}
		}
	}
	return false
}

func equal(a, b []int) bool {
	for i := 0; i < len(a); i++ {
		if a[i] != b[i] {
			return false
		}
	}
	return true
}