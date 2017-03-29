/*
* @Author: WuLC
* @Date:   2017-03-28 23:54:13
* @Last Modified by:   WuLC
* @Last Modified time: 2017-03-29 12:45:02
*/

# can not deal with multiple highest salary
SELECT Department.Name AS Department, Employee.Name AS Employee, MAX(Employee.Salary) AS Salary \
FROM Employee JOIN Department ON Employee.DepartmentId = Department.Id GROUP BY Employee.DepartmentId;


# with alias name of table to compare its attribute 
SELECT d.Name AS Department, e.Name AS Employee, e.Salary AS Salary 
FROM Employee e, Department d
WHERE e.DepartmentId = d.Id AND e.salary = (SELECT MAX(Salary) FROM Employee se WHERE se.DepartmentId = e.DepartmentId);