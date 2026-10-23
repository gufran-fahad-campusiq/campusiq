-- Day 3: marks and attendance tables + JOIN

CREATE TABLE marks (
  roll_no TEXT REFERENCES students(roll_no),
  subject TEXT,
  internal INT,
  external INT
);
INSERT INTO marks VALUES
('21AI01','ML',34,52),('21AI01','DBMS',30,45),('21AI01','OS',28,40),
('21AI02','ML',25,38),('21AI02','DBMS',31,44),('21AI02','OS',22,30),
('21AI03','ML',38,57),('21AI03','DBMS',36,50),('21AI03','OS',35,55),
('21AI04','ML',20,28),('21AI04','DBMS',24,33),('21AI04','OS',18,25);

CREATE TABLE attendance (
  roll_no TEXT REFERENCES students(roll_no),
  subject TEXT,
  attended INT,
  total INT
);
INSERT INTO attendance VALUES
('21AI01','ML',50,60),('21AI01','DBMS',47,60),('21AI01','OS',45,60),
('21AI02','ML',42,60),('21AI02','DBMS',40,60),('21AI02','OS',36,60),
('21AI03','ML',57,60),('21AI03','DBMS',55,60),('21AI03','OS',54,60),
('21AI04','ML',38,60),('21AI04','DBMS',44,60),('21AI04','OS',33,60);

-- Query 1: total marks of every student in every subject (12 rows)
SELECT s.name, m.subject, m.internal + m.external AS total
FROM students s JOIN marks m ON s.roll_no = m.roll_no
ORDER BY s.name;

-- Query 2: total marks of each student, highest first
SELECT s.name, SUM(m.internal + m.external) AS total_marks
FROM students s JOIN marks m ON s.roll_no = m.roll_no
GROUP BY s.name
ORDER BY total_marks DESC;

-- Query 3: attendance below 75% in any subject
SELECT s.name, a.subject, ROUND(a.attended * 100.0 / a.total, 1) AS pct
FROM students s JOIN attendance a ON s.roll_no = a.roll_no
WHERE a.attended * 100.0 / a.total < 75
ORDER BY pct;