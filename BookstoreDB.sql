/*
Bookstore Database
CS 3380 Project - Phase 3

Name: Andrew Kim
Pawprint: AHKYQX

RDBMS Used: MySQL
*/

-- Create and select database
CREATE SCHEMA STORE_SCHEMA;
USE STORE_SCHEMA;

-- Create tables
CREATE TABLE PUBLISHER (
    P_Name VARCHAR(50),
    Publisher_ID INT NOT NULL,
    Address VARCHAR(50),
    Email VARCHAR(50),
    PRIMARY KEY(Publisher_ID)
    );

CREATE TABLE BOOKSTORE (
    S_Name VARCHAR(50),
    Store_ID INT NOT NULL,
    Address VARCHAR(50),
    Visits INT,
    PRIMARY KEY(Store_ID)
    );

CREATE TABLE MEMBER (
    M_First_name VARCHAR(50),
    M_Last_name VARCHAR(50),
    Member_ID INT NOT NULL AUTO_INCREMENT,
    Reward_points INT,
    Store_ID INT NOT NULL,
    PRIMARY KEY(Member_ID),
    FOREIGN KEY(Store_ID) REFERENCES BOOKSTORE(Store_ID)
    );

CREATE TABLE BOOK (
    Title VARCHAR(50),
    ISBN BIGINT UNSIGNED NOT NULL, 
    Author VARCHAR(50),
    Genre VARCHAR(50),
    Pages INT,
    Price DECIMAL(10,2),
    Store_ID INT NOT NULL,
    Publisher_ID INT NOT NULL,
    PRIMARY KEY(ISBN),
    FOREIGN KEY(Store_ID) REFERENCES BOOKSTORE(Store_ID),
    FOREIGN KEY(Publisher_ID) REFERENCES PUBLISHER(Publisher_ID)
    );

CREATE TABLE EMPLOYEE (
    E_First_name VARCHAR(50),
    E_Middle_initial CHAR(1),
    E_Last_name VARCHAR(50),
    Employee_ID INT NOT NULL AUTO_INCREMENT,
    Birthdate DATE,
    Address VARCHAR(50),
    SSN INT UNIQUE,
    Store_ID INT NOT NULL,
    PRIMARY KEY(Employee_ID),
    FOREIGN KEY(Store_ID) REFERENCES BOOKSTORE(Store_ID)
    );

CREATE TABLE DEPENDENT (
    E_ID INT NOT NULL,
    Dependent_name VARCHAR(50) NOT NULL UNIQUE,
    Birthdate DATE,
    Relationship VARCHAR(50),
    PRIMARY KEY(E_ID, Dependent_name),
    FOREIGN KEY(E_ID) REFERENCES EMPLOYEE(Employee_ID)
    );

CREATE TABLE MEMBER_PHONES (
    Member_ID INT NOT NULL,
    Member_phone CHAR(10) NOT NULL,
    PRIMARY KEY(Member_ID, Member_phone),
    FOREIGN KEY(Member_ID) REFERENCES MEMBER(Member_ID)
    );

-- Insert records into tables
INSERT INTO PUBLISHER VALUES
    ("Penguin Random House LLC", 212782, "1745 Broadway, New York, NY 10019", "consumerservices@penguinrandomhouse.com"),
    ("Scholastic Inc", 812343, "555 Broadway, New York, NY 10012", "slpservice@scholastic.com"),
    ("Macmillan Publishers Inc", 460751, "120 Broadway, New York, NY 10271", "customerservice@mpsvirginia.com");

INSERT INTO BOOKSTORE VALUES
    ("Main Bookstore", 101, "123 E Broadway, Columbia 65201", 1000);

INSERT INTO MEMBER (M_First_name, M_Last_name, Reward_points, Store_ID) VALUES
    ("Thomas", "Johnson", 10, 101),
    ("Sarah", "Clark", 15, 101),
    ("Ronald", "Davidson", 25, 101),
    ("Ann", "Taylor", 35, 101);

INSERT INTO BOOK VALUES
    ("How to Get an A in CS 3380", 6574356098904128, "Andrew Kim", "Nonfiction", 239, 42.39, 101, 212782),
    ("All About MySQL", 1914978970983977, "Praveen Rao", "Nonfiction", 768, 132.99, 101, 812343),
    ("The History of Agriculture", 2862596726766589, "Jim Smith", "Nonfiction", 2304, 70.85, 101, 460751);

INSERT INTO EMPLOYEE (E_First_name, E_Middle_initial, E_Last_name, Birthdate, Address, SSN, Store_ID) VALUES
    ("James", "R", "Smith", "1990-11-22", "100 W Broadway, Columbia, MO 65203", 123456789, 101),
    ("Maria", "F", "Garcia", "2000-12-28", "701 E Broadway, Columbia, MO 65205", 987654321, 101),
    ("Robert", "E", "Brown", "1994-12-13", "3911 Peachtree Drive Columbia, MO 65203", 123987456, 101);

INSERT INTO DEPENDENT VALUES
    (1, "Jimmy Smith", "2020-11-11", "Son"),
    (1, "Josette Brown", "2021-12-29", "Daughter");

INSERT INTO MEMBER_PHONES VALUES
    (1, 5731234567),
    (1, 6181234567),
    (2, 5739876542),
    (3, 3143129847),
    (4, 6184902734);



-- Drop tables/schema
-- DROP TABLE MEMBER, EMPLOYEE, BOOKSTORE, BOOK, PUBLISHER, DEPENDENT, MEMBER_PHONES;
-- DROP SCHEMA STORE_SCHEMA;
