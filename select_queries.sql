-- Activity 1
-- Select all rows and columns from the Exercise table. (64 rows)
SELECT *
FROM exercise;

-- Activity 2
-- Select all rows and columns from the Client table. (500 rows)
SELECT *
FROM client;

-- Activity 3
-- Select all columns from Client where the City is Metairie. (29 rows)
SELECT *
FROM client
WHERE City = 'Metairie';

-- Activity 4
-- Is there a Client with the ClientId '818u7faf-7b4b-48a2-bf12-7a26c92de20c'? (0 rows)
SELECT *
FROM client
WHERE ClientId = '818u7faf-7b4b-48a2-bf12-7a26c92de20c';

-- Activity 5
-- How many rows are in the Goal table? (17 rows)
SELECT *
FROM goal;

-- Activity 6
-- Select Name and LevelId from the Workout table. (26 rows)
SELECT `Name`, LevelID
FROM workout;

-- Activity 7
-- Select Name, LevelId, and Notes from Workout where LevelId is 2. (11 rows)
SELECT `Name`, LevelID, Notes
FROM workout
WHERE LevelID = 2;

-- Activity 8
-- Select FirstName, LastName, and City from Client where City is Metairie, Kenner, or Gretna. (77 rows)
SELECT FirstName, LastName, City
FROM client
WHERE City IN ('Metairie', 'Kenner', 'Gretna');

-- Activity 9
-- Select FirstName, LastName, and BirthDate from Client for Clients born in the 1980s. (72 rows)
SELECT FirstName, LastName, BirthDate
FROM client
WHERE BirthDate >= '1980-1-1' AND BirthDate < '1990-1-1';

-- Activity 10
-- Write the query above in a different way.
SELECT FirstName, LastName, BirthDate
FROM client
WHERE BirthDate BETWEEN '1980-1-1' AND '1990-1-1';

-- Activity 11
-- How many rows in the Login table have a .gov EmailAddress? (17 rows)
SELECT *
FROM login
WHERE EmailAddress LIKE '%.gov';

-- Activity 12
-- How many Logins do NOT have a .com EmailAddress? (122 rows)
SELECT *
FROM login
WHERE EmailAddress NOT LIKE '%.com';

-- Activity 13
-- Select first and last name of Clients without a BirthDate. (37 rows)
SELECT FirstName, LastName
FROM client
WHERE BirthDate IS NULL;

-- Activity 14
-- Select the Name of each ExerciseCategory that has a parent (ParentCategoryId value is not null). (12 rows)
SELECT `Name`
FROM exercisecategory
WHERE ParentCategoryId IS NOT NULL;

-- Activity 15
-- Select Name and Notes of each level 3 Workout that contains the word 'you' in its Notes. (4 rows)
SELECT `Name`, Notes
FROM workout
WHERE LevelId = 3 AND notes LIKE '%you%';

-- Activity 16
-- Select FirstName, LastName, City from Client whose LastName starts with L,M, or N and who live in LaPlace. (5 rows)
SELECT FirstName, LastName, City
FROM client
WHERE (LastName LIKE 'L%' OR LastName LIKE 'M%' OR LastName LIKE 'N%')
    AND City = 'LaPlace';

-- Activity 17
-- Select InvoiceId, Description, Price, Quantity, ServiceDate and the line item total, 
-- a calculated value, from InvoiceLineItem, where the line item total is between 15 and 25 dollars. (667 rows)
SELECT InvoiceId, `Description`, Price, Quantity, ServiceDate, Price * Quantity AS line_item_total
FROM invoicelineitem
WHERE Price * Quantity BETWEEN 15 AND 25;

-- Activity 18
-- Does the database include an email address for the Client, Estrella Bazely?
-- Select a Client record for Estrella Bazely. Does it exist?
SELECT ClientID
FROM client
WHERE FirstName = 'Estrella' AND LastName = 'Bazely';
-- If it does, select a Login record that matches its ClientId.
SELECT EmailAddress
FROM login
WHERE ClientID = '87976c42-9226-4bc6-8b32-23a8cd7869a5';

-- Activity 19
-- What are the Goals of the Workout with the Name 'This Is Parkour'?
-- Select the WorkoutId from Workout where Name equals 'This Is Parkour'. (1 row)
SELECT WorkoutID
FROM workout
WHERE `Name` = 'This Is Parkour';
-- Select GoalId from WorkoutGoal where the WorkoutId matches the WorkoutId from your first query. (3 rows)
SELECT GoalID
FROM workoutgoal
WHERE WorkoutId = 12;
-- Select the goal name from Goal where the GoalId is one of the GoalIds from your second query. (3 rows)
SELECT `Name`
FROM goal
WHERE GoalId IN (3,8,15);