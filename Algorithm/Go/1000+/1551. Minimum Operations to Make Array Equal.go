func minOperations(n int) int {
	i, result := 0, 0
	for i < (n >> 1) {
		result += n - 2*i - 1
		i++
	}
	return result
}