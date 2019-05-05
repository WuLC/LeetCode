/*
 * Created on Sun May 05 2019 16:52:21
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

 // sort with custom compare function
import "sort"

func twoCitySchedCost(costs [][]int) int {
	sort.SliceStable(costs, func(i, j int) bool {
		return costs[i][0] - costs[i][1] < costs[j][0] - costs[j][1]
	})
	result, half := 0, len(costs)>>1
	for i := 0; i < half; i++ {
		result += costs[i][0] + costs[i+half][1]
	}
	return result
}