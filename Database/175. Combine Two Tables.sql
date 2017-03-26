/*
* @Author: WuLC
* @Date:   2017-03-26 12:48:01
* @Last Modified by:   WuLC
* @Last Modified time: 2017-03-26 12:48:42
*/

# typical left join
SELECT Person.FirstName, Person.LastName, Address.City, Address.State FROM Person LEFT JOIN Address ON Person.PersonId = Address.PersonId;