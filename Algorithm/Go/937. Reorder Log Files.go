/*
 * Created on Fri Nov 16 2018 19:44:26
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

// strings.Index to locate the index of certain string
// sort.Slice to use custom sort function
package main

import (
	"fmt"
	"sort"
	"strings"
	"unicode"
)

func reorderLogFiles(logs []string) []string {
	var letter_logs []string
	var digital_logs []string
	for _, s := range logs {
		if unicode.IsDigit(rune(s[len(s)-1])) {
			digital_logs = append(digital_logs, s)
		} else {
			letter_logs = append(letter_logs, s)
		}
	}
	sort.Slice(letter_logs, func(i, j int) bool {
		return letter_logs[i][strings.Index(letter_logs[i], " "):] < letter_logs[j][strings.Index(letter_logs[j], " "):]
	})

	return append(letter_logs, digital_logs...)
	// the following code is the same as the above line
	// for i := 0; i < len(digital_logs); i++ {
	// 	letter_logs = append(letter_logs, digital_logs[i])
	// }
	// return letter_logs
}
