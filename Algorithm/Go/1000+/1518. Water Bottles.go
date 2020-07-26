func numWaterBottles(numBottles int, numExchange int) int {
	result, emptyBottles := numBottles, numBottles
	for emptyBottles >= numExchange {
		exchanged, remainder := emptyBottles/numExchange, emptyBottles%numExchange
		emptyBottles = exchanged + remainder
		result += exchanged
	}
	return result
}