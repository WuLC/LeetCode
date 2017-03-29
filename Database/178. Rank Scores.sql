# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2017-03-29 20:15:36
# @Last modified by:   WuLC
# @Last Modified time: 2017-03-29 20:15:38
# @Email: liangchaowu5@gmail.com


SELECT Score, (SELECT count(*) FROM (SELECT distinct Score s FROM Scores) WHERE s >= Score) AS Rank
FROM Scores ORDER BY Score DESC;

# the above line has the following error
# Every derived table must have its own alias
# thus need to be modified as follows
SELECT Score, (SELECT count(*) FROM (SELECT distinct Score s FROM Scores) AS tmp WHERE s >= Score) AS Rank
FROM Scores ORDER BY Score DESC;