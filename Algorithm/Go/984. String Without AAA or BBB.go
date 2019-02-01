/*
 * Created on Fri Feb 01 2019 7:59:46
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

 // greedy
 import "bytes"

 func strWithout3a3b(A int, B int) string {
	 result := bytes.NewBufferString("")
	 for A>0 || B>0 {
		 if A == B {
			 result.WriteString("ab")
			 A--
			 B--
		 } else if A > B {
			 if A > 1 {
				 result.WriteString("aa")
			 } else {
				 result.WriteString("a")
			 }
			 if B > 0 {
				 result.WriteString("b")
			 } else {
				 result.WriteString("")
			 }
			 A -= 2
			 B -= 1
		 } else {
			 if B > 1 {
				 result.WriteString("bb")
			 } else {
				 result.WriteString("b")
			 }
			 if A > 0 {
				 result.WriteString("a")
			 } else {
				 result.WriteString("")
			 }
			 A -= 1
			 B -= 2
		 }
	 }
	 return result.String()
 }