CREATE TABLE students (
  roll_no TEXT PRIMARY KEY,
  name TEXT,
  branch TEXT,
  cgpa NUMERIC(3,1)
);
INSERT INTO students VALUES
('21AI01','Ravi','AIML',8.4),
('21AI02','Asha','AIML',7.2),
('21AI03','Imran','AIML',9.1),
('21AI04','Zoya','AIML',6.8);

SELECT * FROM students;
SELECT name FROM students WHERE cgpa > 8;
SELECT AVG(cgpa) FROM students;