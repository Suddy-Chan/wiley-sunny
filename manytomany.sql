CREATE DATABASE school;
USE school;

CREATE TABLE Student (
	StudentID INT PRIMARY KEY AUTO_INCREMENT,
    FirstName VARCHAR(30) NOT NULL,
    LastName VARCHAR(30) NOT NULL,
    Major VARCHAR(60) NOT NULL
);

CREATE TABLE Class (
	ClassID INT PRIMARY KEY AUTO_INCREMENT,
    Course VARCHAR(30) NOT NULL,
    `DateTime` DATETIME,
    Room VARCHAR(6),
    Term VARCHAR(6)
);

CREATE TABLE Enrollment (
	StudentID INT NOT NULL,
    ClassID INT NOT NULL,
    PRIMARY KEY pk_StudentClass (StudentID, ClassID),
    FOREIGN KEY fk_StudentClass_Student (StudentID)
        REFERENCES Student(StudentID),
	FOREIGN KEY fk_StudentClass_Class (ClassID)
        REFERENCES Class(ClassID)
);
