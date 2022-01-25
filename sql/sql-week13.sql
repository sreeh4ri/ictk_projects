-- 1. Create Employee Table
CREATE TABLE Employee (
    id INT AUTO_INCREMENT PRIMARY KEY,
    `Employee ID` VARCHAR(6) UNIQUE NOT NULL,
    Name VARCHAR(50) NOT NULL,
    Gender VARCHAR(1),
    Department VARCHAR(50),
    Salary INT,
    DOB VARCHAR(15),
    `Date of Joining` VARCHAR(15)
);
insert into Employee ( `Employee ID`, Name, Gender, Department, Salary, DOB, `Date of Joining`) values
('CP0123', 'Ann Mery', 'F', 'HR', 45000,'10/Oct/1989', '01/Jan/2018'),
('CP0087', 'Felix M', 'M', 'Finance', 48000, '12/Oct/1981', '10/DEC/2000'),
('CP0197', 'Merlin', 'F', 'CEO', 80000,'01/Mar/1990', '10/May/2011'),
('CP0213', 'Philip', 'M', 'Retail', 47000,'01/Apr/1991', '01/Jun/2012'),
('CP0243', 'Michael', 'M', 'Retail', 40000,'10/Oct/1992', '01/May/2016'),
('CP0289', 'Susan', 'F', 'Retail', 40000,'01/Jan/1991', '01/Apr/2016'),
('CP0298', 'Abram', 'M', 'Relations', 30000,'17/Apr/1994', '06/Oct/2016'),
('CP0300', 'Alia', 'F', 'Relation', 30000,'17/Oct/1995', '18/Oct/2016'),
('CP0321', 'Raichal', 'F', 'Marketing', 34000,'09/Oct/1990', '22/Oct/2016'),
('CP0276', 'Thomas', 'M', 'Marketing', 44000,'19/Nov/1983', '22/Oct/2018');

-- 2. Write SQL queries to select employess from a. Maketing, b. Retail, c.HR departments.
SELECT 
    *
FROM
    employee
WHERE
    Department IN ('Marketing' , 'HR', 'Retail');

-- 3. Write SQL query to create a table only containing female employee.alter
CREATE TABLE Female_Employees AS SELECT * FROM
    employee
WHERE
    Gender = 'F';

-- 4. Write SQL query to display Maximum, Minimum and Average salary
SELECT 
    MAX(Salary), MIN(Salary), AVG(Salary)
FROM
    employee;
    
-- 5. Write SQL query to display info based on following conditions
-- a. Male employees having salary greater than 40000
SELECT 
    *
FROM
    employee
WHERE
    Gender = 'M' AND Salary > 40000;
    
-- b. Female employees havng salary less than 45000
SELECT 
    *
FROM
    employee
WHERE
    Gender = 'F' AND Salary < 45000;
    
-- c. Employee having salary between 30000 and 60000 and working in Marketing or Retail department
SELECT 
    *
FROM
    employee
WHERE
    Salary BETWEEN 30000 AND 60000
        AND Department IN ('Marketing' , 'Retail')