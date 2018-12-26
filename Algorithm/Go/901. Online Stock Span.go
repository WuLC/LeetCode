/*
 * Created on Wed Dec 26 2018 19:10:41
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

// keep decreasing elements in a stack

type StockSpanner struct {
	stack [][]int
	count int
}

func Constructor() StockSpanner {
	return StockSpanner{[][]int{}, 0}
}

func (this *StockSpanner) Next(price int) int {
	this.count++
	n := len(this.stack)
	for n > 0 && this.stack[n-1][0] <= price {
		n--
		this.stack = this.stack[:n]
	}
	result := this.count
	if n > 0 {
		result = this.count - this.stack[n-1][1]
	}
	this.stack = append(this.stack, []int{price, this.count})
	return result
}

/**
 * Your StockSpanner object will be instantiated and called as such:
 * obj := Constructor();
 * param_1 := obj.Next(price);
 */
