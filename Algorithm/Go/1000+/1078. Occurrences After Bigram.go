/*
 * Created on Sun Jun 09 2019 17:57:41
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

import "strings"

func findOcurrences(text string, first string, second string) []string {
	words := strings.Split(text, " ")
	result := []string{}
	for i := 0; i < len(words) - 2; i++ {
		if words[i] == first && words[i+1] == second {
			result = append(result, words[i+2])
		}
	}
	return result
}