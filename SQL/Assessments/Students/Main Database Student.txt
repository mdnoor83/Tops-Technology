CREATE DATABASE IF NOT EXISTS School;

USE School;

CREATE TABLE IF NOT EXISTS Student (
    StdID INT PRIMARY KEY,
    StdName VARCHAR(255),
    Sex VARCHAR(10),
    Percentage DECIMAL(5, 2),
    Class VARCHAR(10),
    Sec CHAR(1),
    Stream VARCHAR(50),
    DOB DATE
);

INSERT INTO Student (StdID, StdName, Sex, Percentage, Class, Sec, Stream, DOB) VALUES
(1001, 'Surekha Joshi', 'Female', 82.00, '12', 'A', 'Science', '1998-08-03'),
(1002, 'Maahi Agarwal', 'Female', 56.00, '11', 'C', 'Commerce', '2008-11-30'),
(1003, 'Sanam Verma', 'Male', 59.00, '11', 'C', 'Commerce', '2006-06-29'),
(1004, 'Ronir Kumar', 'Male', 63.00, '11', 'C', 'Commerce', '1997-05-11'),
(1005, 'Dipesh Pulkit', 'Male', 78.00, '11', 'B', 'Science', '2003-09-14'),
(1006, 'Jahanvi Puri', 'Female', 60.00, '11', 'B', 'Commerce', '2008-11-07'),
(1007, 'Sanam Kumar', 'Male', 23.00, '12', 'F', 'Commerce', '1998-08-03'),
(1008, 'Sahil Saras', 'Male', 56.00, '11', 'C', 'Commerce', '2008-07-11'),
(1009, 'Akshra Agarwal', 'Female', 72.00, '12', 'B', 'Commerce', '1996-01-10'),
(1010, 'Stuti Mishra', 'Female', 39.00, '11', 'F', 'Science', '2008-11-30'),
(1011, 'Harsh Agarwal', 'Male', 42.00, '11', 'C', 'Science', '1998-06-28'),
(1012, 'Nikunj Agarwal', 'Male', 49.00, '12', 'C', 'Commerce', '1998-06-28'),
(1013, 'Akriti Saxena', 'Female', 89.00, '12', 'A', 'Science', '2008-11-30'),
(1014, 'Tani Rastogi', 'Female', 82.00, '12', 'A', 'Science', '2008-11-30');
