/*
* @Author: WuLC
* @Date:   2017-03-20 00:25:02
* @Last Modified by:   WuLC
* @Last Modified time: 2017-03-20 00:25:23
*/

# inner joint on the same table
SELECT a.Name AS Employee FROM Employee a JOIN Employee b on a.ManagerId = b.Id where a.Salary > b.Salary;