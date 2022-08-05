-- Part 2: Define the Database
-- Delete 'Hotel' database if exists
DROP DATABASE Hotel;

-- Create new database called 'Hotel'
CREATE DATABASE Hotel;

-- Use the database 'Hotel'
USE Hotel;

-- Create 'Room' Table
CREATE TABLE Room (
	RoomNumber INT PRIMARY KEY,
    `Type` CHAR(10) NOT NULL,
    Amenities VARCHAR(60) NOT NULL,
    ADA_Accessible BOOL NOT NULL DEFAULT 1,
    StandardOccupancy INT NOT NULL,
    MaximumOccupancy INT NOT NULL,
    BasePrice VARCHAR(10) NOT NULL,
    ExtraPerson VARCHAR(10) NULL
);

-- Create 'Guest' Table
CREATE TABLE Guest (
	`Name` VARCHAR(30) PRIMARY KEY,
	Address VARCHAR(30) NOT NULL,
    City VARCHAR(20) NOT NULL,
    State CHAR(2) NOT NULL,
    Zip CHAR(5) NOT NULL,
    Phone CHAR(15) NOT NULL
);

-- CREATE 'Reservation' Table
-- Foreign keys: RoomNumber, `Name`
CREATE TABLE Reservation (
	ReservationID INT PRIMARY KEY AUTO_INCREMENT,
	RoomNumber INT NOT NULL,
    `Name` VARCHAR(30) NOT NULL,
    Adults INT NOT NULL,
    Children INT NOT NULL,
    StartDate DATE NOT NULL,
    EndDate DATE NOT NULL,
    TotalRoomCost VARCHAR(10) NOT NULL,
    CONSTRAINT fk_Reservation_Room FOREIGN KEY (RoomNumber)
        REFERENCES Room(RoomNumber),
	CONSTRAINT fk_Reservation_Guest FOREIGN KEY (`Name`)
        REFERENCES Guest(`Name`)
);
    
-- END of Part 2