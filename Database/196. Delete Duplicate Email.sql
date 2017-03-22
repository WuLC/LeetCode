/*
* @Author: WuLC
* @Date:   2017-03-22 23:50:20
* @Last Modified by:   WuLC
* @Last Modified time: 2017-03-22 23:51:31
*/


# referer: https://discuss.leetcode.com/topic/10964/simple-solution
DELETE p1 FROM Person p1, Person p2 WHERE p1.Email = p2.Email AND p1.Id > p2.Id;