SELECT *
FROM Student
ORDER BY StudentLName ASC;


SELECT StudentID, StudentLName, MoneyBalance
FROM Student
WHERE MoneyBalance < (SELECT AVG(MoneyBalance)
 FROM STUDENT)
ORDER BY MoneyBalance;

SELECT StudentID, DateRecieved
FROM Recieves
WHERE DateRecieved > '2023-08-01' AND ImmName = 'Covid-19'
GROUP BY StudentID;


SELECT COUNT(ImmName), ImmName
FROM Recieves
WHERE DateRecieved > '2023-07-30'
GROUP BY ImmName;

SELECT T.TeacherName, ClassNo, HallwayName
FROM Teacher T RIGHT OUTER JOIN Classroom C
ON T.TeacherID = C.TeacherID
ORDER BY HallwayName, ClassNo;

SELECT S.StudentID, S.StudentFName, S.StudentLName, B.BusNo, B.DepartTime
FROM Student S, Bus B
WHERE S.BusNo = B.BusNo AND S.TeacherID = '110'
ORDER BY DepartTime;

DROP VIEW bus_depart_time_at_1430_students;
DROP VIEW bus_depart_times_Mrs_Lazarus_students;

CREATE VIEW bus_depart_times_Mrs_Lazarus_students AS
SELECT S.StudentID, S.StudentFName, S.StudentLName, B.BusNo, B.DepartTime
FROM Student S, Bus B
WHERE S.BusNo = B.BusNo AND S.TeacherID = '110'
ORDER BY DepartTime;
SELECT *
FROM bus_depart_times_Mrs_Lazarus_students;

CREATE VIEW bus_depart_time_at_1430_students AS
SELECT S.StudentID, S.StudentFName, S.StudentLName, B.BusNo, B.DepartTime
FROM Student S, Bus B
WHERE S.BusNo = B.BusNo AND B.DepartTime = '14:30'
ORDER BY DepartTime;

SELECT *
FROM bus_depart_times_mrs_lazarus_students
UNION
SELECT *
FROM bus_depart_time_at_1430_students;

DROP PROCEDURE IF EXISTS students_age;

DELIMITER //
CREATE PROCEDURE students_age()
	BEGIN
		SELECT StudentLName, Birthdate, CURDATE(),
        TIMESTAMPDIFF(YEAR, Birthdate, CURDATE()) AS Age
        FROM Student
        ORDER BY Birthdate;
	END //
DELIMITER ;
CALL students_age();

DROP FUNCTION IF EXISTS age_of_students;
CREATE FUNCTION age_of_students(date1 DATE) 
	RETURNS INT DETERMINISTIC
    RETURN year(CURDATE()) - year(date1);
	
SELECT StudentID, StudentLName, age_of_students(Birthdate) AS Age
FROM Student;