import "sort"
func maxIceCream(costs []int, coins int) int {
    sort.Ints(costs)
    result := 0
    for _, c := range costs {
        if c > coins {
            break
        }
        coins -= c
        result++
    }
    return result
}