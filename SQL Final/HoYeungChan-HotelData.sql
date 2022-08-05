-- Part 3: Manage the Data
-- USE database 'Hotel'
USE Hotel;

-- Add data to 'Room' table
INSERT INTO Room (RoomNumber, `Type`, Amenities, ADA_Accessible,
StandardOccupancy, MaximumOccupancy, BasePrice, ExtraPerson)
VALUES
(201,'Double','Microwave, Jacuzzi',0,2,4,'$199.99','$10'),
(202,'Double','Refrigerator',1,2,4,'$174.99','$10'), 
(203,'Double','Microwave, Jacuzzi',0,2,4,'$199.99','$10'),
(204,'Double','Refrigerator',1,2,4,'$174.99','$10'),
(205,'Single','Microwave, Refrigerator, Jacuzzi',0,2,2,'$174.99',NULL),
(206,'Single','Microwave, Refrigerator',1,2,2,'$149.99',NULL),
(207,'Single','Microwave, Refrigerator, Jacuzzi',0,2,2,'$174.99',NULL),
(208,'Single','Microwave, Refrigerator',1,2,2,'$149.99',NULL),
(301,'Double','Microwave, Jacuzzi',0,2,4,'$199.99','$10'),
(302,'Double','Refrigerator',1,2,4,'$174.99','$10'),
(303,'Double','Microwave, Jacuzzi',0,2,4,'$199.99','$10'), 
(304,'Double','Refrigerator',1,2,4,'$174.99','$10'),
(305,'Single','Microwave, Refrigerator, Jacuzzi',0,2,2,'$174.99',NULL),
(306,'Single','Microwave, Refrigerator',1,2,2,'$149.99',NULL),
(307,'Single','Microwave, Refrigerator, Jacuzzi',0,2,2,'$174.99',NULL),
(308,'Single','Microwave, Refrigerator',1,2,2,'$149.99',NULL),
(401,'Suite','Microwave, Refrigerator, Oven',1,3,8,'$399.99','$20'),
(402,'Suite','Microwave, Refrigerator, Oven',1,3,8,'$399.99','$20');

-- ADD data to 'Guest' Table
INSERT INTO Guest (`Name`, Address, City, State, Zip, Phone)
VALUES
('Sunny Chan','123 Long Street','San Francisco','CA','34567','(321) 239-4959'),
('Mack Simmer','379 Old Shore Street','Council Bluffs','IA','51501','(291) 553-0508'),
('Bettyann Seery','750 Wintergreen Dr.','Wasilla','AK','99654','(478) 277-9632'),
('Duane Cullison','9662 Foxrun Lane','Harlingen','TX','78552','(308) 494-0198'),
('Karie Yang','9378 W. Augusta Ave.','West Deptford','NJ','8096','(214) 730-0298'),
('Aurore Lipton','762 Wild Rose Street','Saginaw','MI','48601','(377) 507-0974'),
('Zachery Luechtefeld','7 Poplar Dr.','Arvada','CO','80003','(814) 485-2615'),
('Jeremiah Pendergrass','70 Oakwood St.','Zion','IL','60099','(279) 491-0960'),
('Walter Holaway','7556 Arrowhead St.','Cumberland','RI','2864','(446) 396-6785'),
('Wilfred Vise','77 West Surrey Street','Oswego','NY','13126','(834) 727-1001'),
('Maritza Tilton','939 Linda Rd.','Burke','VA','22015','(446) 351-6860'),
('Joleen Tison','87 Queen St.','Drexel Hill','PA','19026','(231) 893-2755');

-- Add data to 'Reservation' table
INSERT INTO Reservation
(RoomNumber, `Name`, Adults, Children, StartDate, EndDate, TotalRoomCost)
VALUES
(308,'Mack Simmer',1,0,'2023-2-2','2023-2-4','$299.98'),
(203,'Bettyann Seery',2,1,'2023-2-5','2023-2-10','$999.95'),
(305,'Duane Cullison',2,0,'2023-2-22','2023-2-24','$349.98'),
(201,'Karie Yang',2,2,'2023-3-6','2023-3-7','$199.99'),
(307,'Sunny Chan',1,1,'2023-3-17','2023-3-20','$524.97'),
(302,'Aurore Lipton',3,0,'2023-3-18','2023-3-23','$924.95'),
(202,'Zachery Luechtefeld',2,2,'2023-3-29','2023-3-31','$349.98'),
(304,'Jeremiah Pendergrass',2,0,'2023-3-31','2023-4-5','$874.95'),
(301,'Walter Holaway',1,0,'2023-4-9','2023-4-13','$799.96'),
(207,'Wilfred Vise',1,1,'2023-4-23','2023-4-24','$174.99'),
(401,'Maritza Tilton',2,4,'2023-5-30','2023-6-2','$1,199.97'),
(206,'Joleen Tison',2,0,'2023-6-10','2023-6-14','$599.96'),
(208,'Joleen Tison',1,0,'2023-6-10','2023-6-14','$599.96'),
(304,'Aurore Lipton',3,0,'2023-6-17','2023-6-18','$184.99'),
(205,'Sunny Chan',2,0,'2023-6-28','2023-7-2','$699.96'),
(204,'Walter Holaway',3,1,'2023-7-13','2023-7-14','$184.99'),
(401,'Wilfred Vise',4,2,'2023-7-18','2023-7-21','$1,259.97'),
(303,'Bettyann Seery',2,1,'2023-7-28','2023-7-29','$199.99'),
(305,'Bettyann Seery',1,0,'2023-8-30','2023-9-1','$349.98'),
(208,'Mack Simmer',2,0,'2023-9-16','2023-9-17','$149.99'),
(203,'Karie Yang',2,2,'2023-9-13','2023-9-15','$399.98'),
(401,'Duane Cullison',2,2,'2023-11-22','2023-11-25','$1,199.97'),
(206,'Mack Simmer',2,0,'2023-11-22','2023-11-25','$449.97'),
(301,'Mack Simmer',2,2,'2023-11-22','2023-11-25','$599.97'),
(302,'Maritza Tilton',2,0,'2023-12-24','2023-12-28','$699.96'); 

-- Delete Jeremiah Pendergrass and his reservations
-- Delete his reservations from 'Reservation' table first
DELETE FROM Reservation
WHERE `Name` = 'Jeremiah Pendergrass';

-- Then delete him from 'Guest' table
DELETE FROM Guest
WHERE `Name` = 'Jeremiah Pendergrass';

-- END of Part 3