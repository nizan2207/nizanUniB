--- Q1
SELECT licenseplate FROM rent where licenseplate in (SELECT licenseplate FROM Bulldozer WHERE onedayrentcost>1400 AND typeid in (SELECT typeid FROM bulldozertype WHERE name = 'Tractor N3')) group by licenseplate having count (distinct contactguyid) >= 7;

--- Q2
SELECT typeid, name FROM bulldozertype WHERE typeid in (select typeid FROM bulldozer WHERE licenseplate not in (SELECT licenseplate From rent WHERE rentdate >= '2012-01-01'));

--- Q3
SELECT companyname FROM customer WHERE companyid IN (SELECT companyid FROM contactguy WHERE id IN (SELECT contactguyid FROM (SELECT MAX((calc.returndate-calc.rentdate)*calc.onedayrentcost) as f, calc.contactguyid FROM (SELECT rent.*, bulldozer.onedayrentcost FROM rent join bulldozer on rent.licenseplate = bulldozer.licenseplate) as calc GROUP BY (calc.contactguyid)) as calc WHERE f = (SELECT MAX((calc.returndate-calc.rentdate)*calc.onedayrentcost) as f FROM (SELECT rent.*, bulldozer.onedayrentcost FROM rent join bulldozer on rent.licenseplate = bulldozer.licenseplate) as calc) GROUP BY (calc.contactguyid)));

--- Q4
ALTER TABLE bulldozertype
DROP CONSTRAINT "FK2";
ALTER TABLE bulldozertype
ADD CONSTRAINT "FK2"
FOREIGN KEY (employeeid)
REFERENCES employee (id)
ON DELETE SET NULL;

DELETE FROM employee WHERE id = 9999;

--- Q5
INSERT INTO employee VALUES (1111,'Levy','Avi','HaYarkon 11, Haifa',0551234567,'1988-11-11',11000);

--- Q6
UPDATE bulldozertype SET employeeid = 1111 WHERE name = 'superbull';

--- Q7
SELECT site_id FROM ProductPrice WHERE from_date < '2016-01-01' AND (to_date >= '2015-01-01' OR to_date IS NULL) GROUP BY site_id HAVING COUNT(p_id)<100;

--- Q8
SELECT MAX(price)-MIN(price) AS MaxMinDiff FROM ProductPrice WHERE p_id = 18 AND to_date IS NULL;

--- Q9
SELECT p_id FROM productprice WHERE (from_date < '2015-11-01') AND p_id NOT IN(SELECT p_id FROM productprice WHERE NOT( from_date < '2015-11-01')) GROUP BY p_id;

--- Q10
SELECT site_id FROM (SELECT COUNT(site_id) AS numofpinsite,site_id FROM ProductPrice WHERE from_date < '2016-01-01' AND (to_date >= '2015-01-01' OR to_date IS NULL) GROUP BY site_id) AS FinalAnswer WHERE FinalAnswer.numofpinsite = (SELECT MAX(SitePCount.numofpinsite) AS maxP FROM (SELECT COUNT(site_id) AS numofpinsite,site_id FROM ProductPrice WHERE from_date < '2016-01-01' AND (to_date >= '2015-01-01' OR to_date IS NULL) GROUP BY site_id) AS SitePCount);