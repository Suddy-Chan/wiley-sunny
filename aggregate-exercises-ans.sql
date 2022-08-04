use PersonalTrainer;

-- Use an aggregate to count the number of Clients.
-- 500 rows
--------------------
SELECT COUNT(*)
FROM Client;

-- Use an aggregate to count Client.BirthDate.
-- The number is different than total Clients. Why?
-- 463 rows
--------------------
SELECT COUNT(BirthDate)
FROM Client;
-- Different because it excludes NULL values

-- Group Clients by City and count them.
-- Order by the number of Clients desc.
-- 20 rows
--------------------
SELECT City, COUNT(City)
FROM Client
GROUP BY City
ORDER BY COUNT(City) DESC;

-- Calculate a total per invoice using only the InvoiceLineItem table.
-- Group by InvoiceId.
-- You'll need an expression for the line item total: Price * Quantity.
-- Aggregate per group using SUM().
-- 1000 rows
--------------------
SELECT InvoiceId, SUM(Price * Quantity) TotalPerInvoice
FROM InvoiceLineItem
GROUP BY InvoiceId;

-- Calculate a total per invoice using only the InvoiceLineItem table.
-- (See above.)
-- Only include totals greater than $500.00.
-- Order from lowest total to highest.
-- 234 rows
--------------------
SELECT InvoiceId, SUM(Price * Quantity) TotalPerInvoice
FROM InvoiceLineItem
GROUP BY InvoiceId
HAVING SUM(Price * Quantity) > 500.00
ORDER BY SUM(Price * Quantity);

-- Calculate the average line item total
-- grouped by InvoiceLineItem.Description.
-- 3 rows
--------------------
SELECT `Description`, AVG(Price * Quantity) AverageLineItemTotal
FROM InvoiceLineItem
GROUP BY `Description`;

-- Select ClientId, FirstName, and LastName from Client
-- for clients who have *paid* over $1000 total.
-- Paid is Invoice.InvoiceStatus = 2.
-- Order by LastName, then FirstName.
-- 146 rows
--------------------
SELECT c.ClientID, c.FirstName, c.LastName, SUM(li.Price * li.Quantity) Total
FROM client c
INNER JOIN Invoice i
	ON c.ClientId = i.ClientId
INNER JOIN InvoiceLineItem li
	ON i.InvoiceId = li.InvoiceId
WHERE i.InvoiceStatus = 2
GROUP BY c.ClientId
HAVING SUM(li.Price * li.Quantity) > 1000
ORDER BY c.LastName, c.FirstName;

-- Count exercises by category.
-- Group by ExerciseCategory.Name.
-- Order by exercise count descending.
-- 13 rows
--------------------
SELECT c.Name CategoryName, COUNT(e.ExerciseId) ExerciseCount
FROM ExerciseCategory c
INNER JOIN Exercise e
	ON c.ExerciseCategoryId = e.ExerciseCategoryId
GROUP BY c.Name
ORDER BY COUNT(e.ExerciseId) DESC;

-- Select Exercise.Name along with the minimum, maximum,
-- and average ExerciseInstance.Sets.
-- Order by Exercise.Name.
-- 64 rows
--------------------
SELECT e.Name ExerciseName, MIN(i.Sets) SetsMIN, MAX(i.Sets) SetsMAX, AVG(i.Sets) SetsAVG
FROM Exercise e
INNER JOIN ExerciseInstance i
	ON e.ExerciseId = i.ExerciseId
GROUP BY e.ExerciseId
ORDER BY e.Name;

-- Find the minimum and maximum Client.BirthDate
-- per Workout.
-- 26 rows
-- Sample: 
-- WorkoutName, EarliestBirthDate, LatestBirthDate
-- '3, 2, 1... Yoga!', '1928-04-28', '1993-02-07'
--------------------
SELECT 
	w.Name WorkoutName, 
	MIN(c.BirthDate) EarliestBirthDate, 
	MAX(c.BirthDate) LatestBirthDate 
FROM Workout w
INNER JOIN ClientWorkout cw
	ON w.WorkoutId = cw.WorkoutId
INNER JOIN Client c
	ON cw.ClientId = c.ClientId
GROUP BY w.WorkoutId
ORDER BY w.Name;

-- Count client goals.
-- Be careful not to exclude rows for clients without goals.
-- 500 rows total
-- 50 rows with no goals
--------------------
SELECT c.ClientId, COUNT(cg.GoalId) GoalCount
FROM Client c
LEFT OUTER JOIN ClientGoal cg
	ON c.ClientId = cg.ClientId
GROUP BY c.ClientId
ORDER BY COUNT(cg.GoalId);

-- Select Exercise.Name, Unit.Name, 
-- and minimum and maximum ExerciseInstanceUnitValue.Value
-- for all exercises with a configured ExerciseInstanceUnitValue.
-- Order by Exercise.Name, then Unit.Name.
-- 82 rows
--------------------
SELECT
	e.Name ExerciseName, 
    u.name UnitName,
    MIN(eiuv.value) MinUnitValue,
    MAX(eiuv.value) MaxUnitValue
FROM Exercise e
INNER JOIN ExerciseInstance ei
	ON e.ExerciseId = ei.ExerciseId
INNER JOIN ExerciseInstanceUnitValue eiuv
	ON ei.ExerciseInstanceId = eiuv.ExerciseInstanceId
INNER JOIN Unit u
	ON eiuv.UnitId = u.UnitId
GROUP BY e.ExerciseId, u.UnitId
ORDER BY e.Name, u.Name;

-- Modify the query above to include ExerciseCategory.Name.
-- Order by ExerciseCategory.Name, then Exercise.Name, then Unit.Name.
-- 82 rows
--------------------
SELECT
	c.Name CategoryName,
	e.Name ExerciseName, 
    u.name UnitName,
    MIN(eiuv.value) MinUnitValue,
    MAX(eiuv.value) MaxUnitValue
FROM Exercise e
INNER JOIN ExerciseInstance ei
	ON e.ExerciseId = ei.ExerciseId
INNER JOIN ExerciseInstanceUnitValue eiuv
	ON ei.ExerciseInstanceId = eiuv.ExerciseInstanceId
INNER JOIN Unit u
	ON eiuv.UnitId = u.UnitId
INNER JOIN ExerciseCategory c 
	ON e.ExerciseCategoryId = c.ExerciseCategoryId
GROUP BY e.ExerciseId, u.UnitId, c.ExerciseCategoryId
ORDER BY c.Name, e.Name, u.Name;

-- Select the minimum and maximum age in years for
-- each Level.
-- To calculate age in years, use the MySQL function DATEDIFF.
-- 4 rows
--------------------
SELECT
	l.LevelID, 
    l.Name,
    MIN(DATEDIFF(CURDATE(), c.BirthDate) / 365) MinAge,
    MAX(DATEDIFF(CURDATE(), c.BirthDate) / 365) MaxAge
FROM Level l
INNER JOIN Workout w ON l.LevelId = w.LevelId
INNER JOIN ClientWorkout cw ON w.WorkoutId = cw.WorkoutId
INNER JOIN Client c ON cw.ClientId = c.ClientId
GROUP BY l.LevelID;

-- Stretch Goal!
-- Count logins by email extension (.com, .net, .org, etc...).
-- Research SQL functions to isolate a very specific part of a string value.
-- 27 rows (27 unique email extensions)
--------------------
SELECT
	SUBSTRING_INDEX(EmailAddress, '.', -1),
    COUNT(EmailAddress) EmailCount
FROM Login
GROUP BY SUBSTRING_INDEX(EmailAddress, '.', -1)
ORDER BY COUNT(EmailAddress) DESC;

-- Stretch Goal!
-- Match client goals to workout goals.
-- Select Client FirstName and LastName and Workout.Name for
-- all workouts that match at least 2 of a client's goals.
-- Order by the client's last name, then first name.
-- 139 rows
--------------------
SELECT
	w.Name WorkoutName,
    c.FirstName ClientFirstName,
    c.LastName ClientLastName,
    COUNT(cg.GoalId) ClientGoalCount
FROM Workout w
INNER JOIN WorkoutGoal wg ON w.WorkoutId = wg.WorkoutId
INNER JOIN ClientGoal cg ON wg.GoalId = cg.GoalId
INNER JOIN Client c ON cg.ClientId = c.ClientId
GROUP BY w.WorkoutId , c.ClientId
HAVING COUNT(cg.GoalID) >= 2
ORDER BY c.LastName, c.FirstName;