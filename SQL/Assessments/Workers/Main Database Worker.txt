CREATE DATABASE IF NOT EXISTS projects;

USE projects;

CREATE TABLE Worker (
    Worker_ID INT PRIMARY KEY,
    First_Name VARCHAR(50),
    Last_Name VARCHAR(50),
    Salary DECIMAL(10,2),
    Joining_Date DATE,
    Joining_Time Time,
    Department VARCHAR(50)
);
INSERT INTO Worker VALUES 
('1','Monika', 'Arora', '100000', '2014-02-20','9:00', 'HR'),
('2','Niharika', 'Verma', '80000', '2014-06-11','9:00', 'Admin'),
('3','Vishal', 'Singhal', '300000', '2014-02-20', '9:00', 'HR'),
('4', 'Amitabh', 'Singh', 500000, '2014-02-20', '9:00', 'Admin'),
('5', 'Vivek', 'Bhati', 500000, '2014-06-11', '9:00', 'Admin'),
('6', 'Vipul', 'Diwan', 200000, '2014-06-11', '9:00', 'Account'),
('7', 'Satish', 'Kumar', 75000, '2014-01-20', '9:00', 'Account'),
('8', 'Geetika', 'Chauhan', 90000, '2014-04-11', '9:00', 'Admin');



