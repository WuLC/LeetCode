/*
 * Created on Fri Dec 28 2018 10:20:28
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

package main

func uniqueLetterString(S string) int {
	result := 0
	MOD := 1000000007
	for i := 0; i < len(S); i++ {
		left, right := i-1, i+1
		for left >= 0 && S[left] != S[i] {
			left--
		}
		for right < len(S) && S[right] != S[i] {
			right++
		}
		result += ((i - left) * (right - i)) % MOD
		result %= MOD
	}
	return result
}
