--ניצן בר-אל 322450552
--סעיף 5
CREATE TABLE Customer (
	Customer_id int PRIMARY KEY NOT NULL,
	First_name VARCHAR(255),
	Last_name VARCHAR(255),
	Credit_rating int 
);

CREATE TABLE Employee (
	Employee_id int PRIMARY KEY NOT NULL,
	First_name VARCHAR(255),
	Last_name VARCHAR(255),
	Department_id int,
	Manager_id int,
	CONSTRAINT fk_managerid FOREIGN KEY(Manager_id) REFERENCES Employee(Employee_id),
	CONSTRAINT CHK_NANAGER CHECK (Manager_id <> Employee_id)
);

CREATE TABLE Tree_type(
	Type_id int PRIMARY KEY NOT NULL,
	Description VARCHAR(255) 
);

CREATE TABLE Product(
	Product_id int PRIMARY KEY NOT NULL,
	Description VARCHAR(255),
	Color VARCHAR(255),
	Hight int NOT NULL, 
	Type_id int, 
	Surface_area int,
 	Volume int,
	CONSTRAINT fk_typeid FOREIGN KEY(Type_id) REFERENCES Tree_type(Type_id)
);

CREATE TABLE Department (
	Department_id int PRIMARY KEY NOT NULL,
	Product_id int,
	Dep_manager int,
	CONSTRAINT fk_manager FOREIGN KEY(Dep_manager) REFERENCES Employee(Employee_id),
	CONSTRAINT fk_procuct FOREIGN KEY(Product_id) REFERENCES Product(Product_id)
);

ALTER TABLE Employee
ADD CONSTRAINT fk_departmentid FOREIGN KEY(Department_id) REFERENCES Department(Department_id);

CREATE TABLE Tool(
	Tool_id int PRIMARY KEY NOT NULL,
	Description VARCHAR(255)
);

CREATE TABLE Orders(
	Order_id int NOT NULL,
	Customer_id int NOT NULL,
	Quantity int NOT NULL,
	Product_id int NOT NULL,
	Required_tool int,
	CONSTRAINT pk_Order PRIMARY KEY(Order_id, Customer_id, Quantity, Product_id),
	CONSTRAINT fk_productid FOREIGN KEY(Product_id) REFERENCES Product(Product_id),
	CONSTRAINT fk_tool FOREIGN KEY(Required_tool) REFERENCES Tool(Tool_id)
);
--סעיף 7
INSERT INTO Tool values(1001,'Power saw');
INSERT INTO Tool values(1002, 'Hand saw');
INSERT INTO Tool values(1003, 'Plane');
INSERT INTO Tool values(1004, 'Sander');
INSERT INTO Tool values(1005, 'Hammer');
INSERT INTO Tool values(1006, 'Mallet');
INSERT INTO Tool values(1007, 'Drill');
INSERT INTO Tool values(1008, 'nail');


INSERT INTO Tree_type VALUES(2001, 'Oak');
INSERT INTO Tree_type VALUES(2002, 'Maple');
INSERT INTO Tree_type VALUES(2003, 'Teak');
INSERT INTO Tree_type VALUES(2004, 'Pine');

INSERT INTO Customer VALUES(20, 'Nizan', 'Barel',0);
INSERT INTO Customer VALUES(2, 'Rom', 'Levi',8);
INSERT INTO Customer VALUES(4, 'Ely', 'Morad',35);
INSERT INTO Customer VALUES(6, 'Elad', 'Goldberg',0);
INSERT INTO Customer VALUES(8, 'Nir', 'Shtaine',0);
INSERT INTO Customer VALUES(10, 'Ori', 'Bar',80);
INSERT INTO Customer VALUES(12, 'Yuval', 'Haim',30);
INSERT INTO Customer VALUES(14, 'Niv', 'Kanobi',20);
INSERT INTO Customer VALUES(16, 'Shoval', 'Fader',4);
INSERT INTO Customer VALUES(18, 'Mor', 'Goren',0);

INSERT INTO Employee VALUES(100,'Adam','Abraham');
INSERT INTO Employee VALUES(101,'Adrian','Allan');
INSERT INTO Employee VALUES(102,'Alan','Alsop');
INSERT INTO Employee VALUES(103,'Alexander','Anderson');
INSERT INTO Employee VALUES(104,'Andrew','Arnold');
INSERT INTO Employee VALUES(105,'Anthony','Avery');
INSERT INTO Employee VALUES(106,'Austin','Bailey');
INSERT INTO Employee VALUES(107,'Benjamin','Baker');
INSERT INTO Employee VALUES(108,'Blake','Ball');
INSERT INTO Employee VALUES(109,'Boris','Bell');
INSERT INTO Employee VALUES(110,'Brandon','Berry');
INSERT INTO Employee VALUES(111,'Brian','Black');
INSERT INTO Employee VALUES(112,'Cameron','Bond');
INSERT INTO Employee VALUES(113,'Carl','Bower');
INSERT INTO Employee VALUES(114,'Tim','Brown');
INSERT INTO Employee VALUES(115,'Ronnie','Colman');
--adding a ceo
INSERT INTO Employee VALUES(987654,'Shely','Wiess');

INSERT INTO Product VALUES(4005, 'Table', 'black', 80, 2003, 18000);
INSERT INTO Product VALUES(4006, 'Closet', 'wood', 180, 2004);
--updating the volume for the closet
UPDATE Product SET Volume = 1620000 WHERE Product_id = 4006;
INSERT INTO Product VALUES(4007, 'Chair', 'wood', 40, 2001);
INSERT INTO Product VALUES(4008, 'Bed base', 'wood', 25, 2001, 28000);

INSERT INTO Department VALUES(5005, 4005, 115);
INSERT INTO Department VALUES(5006, 4006, 112);
INSERT INTO Department VALUES(5007, 4007, 103);
INSERT INTO Department VALUES(5008, 4008, 109);

UPDATE Employee SET Manager_id = 115,Department_id = 5005 WHERE Employee_id = 114;
UPDATE Employee SET Manager_id = 115,Department_id = 5005 WHERE Employee_id = 113;
UPDATE Employee SET Manager_id = 114,Department_id = 5005 WHERE Employee_id = 111;
--setting to departmant Manager the ceo as his manager 
UPDATE Employee SET Department_id = 5005, Manager_id = 987654 WHERE Employee_id = 115;
UPDATE Employee SET Manager_id = 112,Department_id = 5006 WHERE Employee_id = 105;
UPDATE Employee SET Manager_id = 112,Department_id = 5006 WHERE Employee_id = 107;
UPDATE Employee SET Manager_id = 107,Department_id = 5006 WHERE Employee_id = 106;
--setting to departmant manager the ceo as his manager
UPDATE Employee SET Department_id = 5006, Manager_id = 987654 WHERE Employee_id = 112;
UPDATE Employee SET Manager_id = 103,Department_id = 5007 WHERE Employee_id = 100;
UPDATE Employee SET Manager_id = 103,Department_id = 5007 WHERE Employee_id = 102;
UPDATE Employee SET Manager_id = 100,Department_id = 5007 WHERE Employee_id = 104;
--setting to departmant manager the ceo as his manager
UPDATE Employee SET Department_id = 5007, Manager_id = 987654 WHERE Employee_id = 103;
UPDATE Employee SET Manager_id = 109,Department_id = 5008 WHERE Employee_id = 108;
UPDATE Employee SET Manager_id = 109,Department_id = 5008 WHERE Employee_id = 110;
UPDATE Employee SET Manager_id = 108,Department_id = 5008 WHERE Employee_id = 101;
--setting to departmant manager the ceo as his manager
UPDATE Employee SET Department_id = 5008, Manager_id = 987654 WHERE Employee_id = 109;

INSERT INTO Orders VALUES(3000,2,1,4005);
INSERT INTO Orders VALUES(3001,2,1,4006);
INSERT INTO Orders VALUES(3002,4,1,4005);
INSERT INTO Orders VALUES(3003,4,1,4006,1005);
INSERT INTO Orders VALUES(3004,4,4,4007);
INSERT INTO Orders VALUES(3005,4,1,4008);
INSERT INTO Orders VALUES(3006,8,1,4005);
INSERT INTO Orders VALUES(3007,8,1,4006);
INSERT INTO Orders VALUES(3008,8,4,4007);
INSERT INTO Orders VALUES(3009,8,3,4008,1001);
INSERT INTO Orders VALUES(3010,6,8,4007);
INSERT INTO Orders VALUES(3011,10,1,4005);
INSERT INTO Orders VALUES(3012,10,6,4007);
INSERT INTO Orders VALUES(3013,12,1,4008);
INSERT INTO Orders VALUES(3014,12,1,4006);
INSERT INTO Orders VALUES(3015,14,2,4008);
INSERT INTO Orders VALUES(3016,14,1,4006);
INSERT INTO Orders VALUES(3017,16,1,4006);
INSERT INTO Orders VALUES(3018,16,1,4008);
INSERT INTO Orders VALUES(3019,18,1,4005);
INSERT INTO Orders VALUES(3020,18,1,4005);





--סעיף 8

SELECT * FROM Product;
SELECT * FROM Employee;
SELECT * FROM Tree_type;

-- select the all of the products description that was oredered by customer with id 2
SELECT Orders.Customer_id, Product.Description 
FROM Product 
FULL OUTER JOIN Orders ON Product.Product_id = Orders.Product_id 
WHERE Orders.Customer_id = 2;

--select the name of all the customers that ordered more than 1 time the product 4005 and print also the product description 
SELECT DES.First_name, DES.Last_name, DES.Description
FROM (SELECT Customer.First_name, Customer.Last_name, Product.Description, Customer.Customer_id
FROM ((Orders
INNER JOIN Customer ON Orders.Customer_id = Customer.Customer_id)
INNER JOIN Product ON Orders.Product_id = Product.Product_id)
WHERE Product.Product_id = 4005) AS DES
GROUP BY DES.Customer_id,DES.First_name, DES.Last_name, DES.Description
HAVING COUNT(DES.Customer_id) > 1;

-- select all the customer information with id grater than 8 and their order id is grater than 3010
SELECT * 
FROM Customer 
WHERE Customer_id IN( SELECT Customer_id
FROM Customer
WHERE Customer_id > 8
INTERSECT
SELECT Customer_id
FROM Orders
WHERE Order_id > 3010);

-- select all the information about customers with id grater than 12 and thier first name start with N
SELECT * 
FROM(SELECT * FROM Customer WHERE First_name LIKE 'N%') AS Cust 
WHERE Customer_id > 12;

-- select the credit rating AND NAME of the customers that bought all of the items
SELECT Credit_rating, First_name, Last_name 
FROM Customer 
WHERE Customer_id IN (SELECT Customer_id FROM Orders WHERE Customer_id IN(SELECT Customer_id FROM Orders WHERE Product_id = 4005) AND Customer_id IN(SELECT Customer_id FROM Orders WHERE Product_id = 4006) AND Customer_id IN(SELECT Customer_id FROM Orders WHERE Product_id = 4007) AND Customer_id IN(SELECT Customer_id FROM Orders WHERE Product_id = 4008) GROUP BY Customer_id);

--select the name and credit rating of all the customers that ordered more times than customer with id 2
SELECT Customer_id, Credit_rating FROM Customer WHERE Customer_id IN(SELECT Customer_id
FROM Orders
GROUP BY Customer_id
HAVING COUNT(Customer_id) > (SELECT COUNT(Customer_id) FROM Orders WHERE Customer_id = 2));

--select the managing tree 
WITH RECURSIVE managers AS (
        SELECT Employee_id, First_name, Last_name, manager_id, 1 AS level
        FROM Employee
        WHERE Employee_id = 987654 -- Shely the ceo
    UNION ALL
        SELECT e.Employee_id, e.First_name, e.Last_name, e.manager_id, managers.level + 1 AS level
        FROM Employee e
        JOIN managers ON e.manager_id = managers.Employee_id
)
SELECT * FROM managers;




--סעיף 14	
WITH ord AS (SELECT Order_id
		, Product_id
		, Quantity
		, ROW_NUMBER() OVER (ORDER BY Order_id ASC) AS row_num
	 FROM Orders )
SELECT 
order1.Order_id
		,order1.Product_id
		,order1.Quantity
		,order2.Order_id as previous_order_id
FROM ord AS order1
LEFT OUTER JOIN ord AS order2
	 ON order1.row_num = (order2.row_num+3);


-- סעיף 15
--Triger
-- First part - create the trigger function (what is the trigger doing)
CREATE OR REPLACE FUNCTION IsToolExist() 
   RETURNS TRIGGER 
   LANGUAGE PLPGSQL
AS $$
DECLARE
sql_quary text;
is_exist TEXT;
BEGIN 
	select COUNT(Tool_id) into is_exist FROM Tool WHERE Tool_id = NEW.Required_tool;
	IF is_exist = '0' THEN
    INSERT INTO Tool values(NEW.Required_tool, 'not specified');
	END IF;
   return new;
END;
$$;
-- Second part - assign the trigger function to an action on a table --
CREATE TRIGGER check_if_tool_exist BEFORE INSERT ON Orders
	for each row EXECUTE FUNCTION IsToolExist();

