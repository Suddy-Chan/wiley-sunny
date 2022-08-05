-- Part 4: Query the Database
-- USE database 'Hotel'
USE Hotel;

-- 1. Write a query that returns a list of reservations that end in July 2023, 
-- including the name of the guest, the room number(s), and the reservation dates.
SELECT `Name`, RoomNumber, StartDate, EndDate
FROM Reservation
WHERE EndDate BETWEEN '2023-07-01' AND '2023-07-31';

-- Q1 Result: (4 rows)
-- Name				RoomNumber		StartDate		EndDate
-- Sunny Chan		205				2023-06-28		2023-07-02
-- Walter Holaway	204				2023-07-13		2023-07-14
-- Wilfred Vise		401				2023-07-18		2023-07-21
-- Bettyann Seery	303				2023-07-28		2023-07-29

-- 2. Write a query that returns a list of all reservations for rooms with a jacuzzi, 
-- displaying the guest's name, the room number, and the dates of the reservation.
SELECT re.`Name`, re.RoomNumber, re.StartDate, re.EndDate
FROM Reservation re
LEFT OUTER JOIN Room ro
	ON re.RoomNumber = ro.RoomNumber
WHERE ro.Amenities LIKE '%jacuzzi%';

-- Q2 Result: (11 rows)
-- Name				RoomNumber	StartDate		EndDate
-- Karie Yang		201			2023-03-06		2023-03-07
-- Bettyann Seery	203			2023-02-05		2023-02-10
-- Karie Yang		203			2023-09-13		2023-09-15
-- Sunny Chan		205			2023-06-28		2023-07-02
-- Wilfred Vise		207			2023-04-23		2023-04-24
-- Walter Holaway	301			2023-04-09		2023-04-13
-- Mack Simmer		301			2023-11-22		2023-11-25
-- Bettyann Seery	303			2023-07-28		2023-07-29
-- Duane Cullison	305			2023-02-22		2023-02-24
-- Bettyann Seery	305			2023-08-30		2023-09-01
-- Sunny Chan		307			2023-03-17		2023-03-20

-- 3. Write a query that returns all the rooms reserved for a specific guest, 
-- including the guest's name, the room(s) reserved, 
-- the starting date of the reservation, and how many people were included in the reservation.
SELECT `Name`, RoomNumber, StartDate, Adults + Children AS PeopleCount
FROM Reservation
WHERE `Name` = 'Bettyann Seery';

-- Q3 Result: (3 rows)
-- Name					RoomNumber		StartDate		PeopleCount
-- Bettyann Seery		203				2023-02-05		3
-- Bettyann Seery		303				2023-07-28		3
-- Bettyann Seery		305				2023-08-30		1

-- 4. Write a query that returns a list of rooms, reservation ID, 
-- and per-room cost for each reservation. The results should include all rooms,
-- whether or not there is a reservation associated with the room.
SELECT ro.RoomNumber, re.ReservationID, re.TotalRoomCost
FROM Room ro
LEFT OUTER JOIN Reservation re
	ON ro.RoomNumber = re.RoomNumber;

-- Q4 Result: (26 rows)
-- RoomNumber 	ReservationID	TotalRoomCost
-- 201			4				$199.99
-- 202			7				$349.98
-- 203			2				$999.95
-- 203			21				$399.98
-- 204			16				$184.99
-- 205			15				$699.96
-- 206			12				$599.96
-- 206			23				$449.97
-- 207			10				$174.99
-- 208			13				$599.96
-- 208			20				$149.99
-- 301			9				$799.96
-- 301			24				$599.97
-- 302			6				$924.95
-- 302			25				$699.96
-- 303			18				$199.99
-- 304			14				$184.99
-- 305			3				$349.98
-- 305			19				$349.98
-- 306			NULL			NULL
-- 307			5				$524.97
-- 308			1				$299.98
-- 401			11				$1,199.97
-- 401			17				$1,259.97
-- 401			22				$1,199.97
-- 402			NULL			NULL

-- 5. Write a query that returns all the rooms accommodating at least three guests
-- and that are reserved on any date in April 2023.
SELECT ro.RoomNumber, COUNT(re.`Name`) GuestCount
FROM Room ro
LEFT OUTER JOIN Reservation re
	ON ro.RoomNumber = re.RoomNumber
WHERE re.StartDate BETWEEN '2023-04-01' AND '2023-04-30'
GROUP BY ro.RoomNumber
HAVING COUNT(re.`Name`) >= 3;

-- Q5 Results: 0 row returned
-- RoomNumber GuestCount

-- 6. Write a query that returns a list of all guest names and the number of reservations per guest, 
-- sorted starting with the guest with the most reservations and then by the guest's last name.
SELECT 
	SUBSTRING_INDEX(`Name`, ' ', 1) FirstName,
    SUBSTRING_INDEX(`Name`, ' ', -1) LastName,
    COUNT(`Name`) ReservationCount
FROM Reservation
GROUP BY `Name`
ORDER BY COUNT(`Name`) DESC, LastName;

-- Q6 Result: (11 rows)
-- FirstName 	LastName 		ReservationCount
-- Mack			Simmer			4
-- Bettyann		Seery			3
-- Sunny		Chan			2
-- Duane		Cullison		2
-- Walter		Holaway			2
-- Aurore		Lipton			2
-- Maritza		Tilton			2
-- Joleen		Tison			2
-- Wilfred		Vise			2
-- Karie		Yang			2
-- Zachery		Luechtefeld		1

-- 7. Write a query that displays the name, address, 
-- and phone number of a guest based on their phone number. 
SELECT `Name`, Address, Phone
FROM Guest
WHERE Phone = '(291) 553-0508';

-- Q7 Result: (1 row)
-- Name 			Address 				Phone
-- Mack Simmer		379 Old Shore Street	(291) 553-0508

-- End of Part 4