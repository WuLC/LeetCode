/*
* @Author: WuLC
* @Date:   2017-03-19 23:48:10
* @Last Modified by:   WuLC
* @Last Modified time: 2017-03-19 23:48:32
*/

# classical method
SELECT Email FROM Person GROUP BY Email HAVING COUNT(Email) > 1;