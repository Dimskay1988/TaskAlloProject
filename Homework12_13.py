create database tmshw12_13
\c tmshw12_13

create table students (
id BIGSERIAL NOT NULL PRIMARY KEY,
first_name VARCHAR(50),
last_name VARCHAR(50),
gender VARCHAR(50),
specialization VARCHAR(50),
date_of_birth DATE
);

INSERT INTO students (first_name, last_name, gender, specialization, date_of_birth) VALUES('Ivan', 'Ivanov','male','Java','2003-03-01'),
('Petya','Petrov','male','Java','1994-01-02'),
('Lena','Lenova','female','Phyton','1998-04-03'),
('Ilon','Mask','male','Phyton','1991-03-12'),
('Maksim','Galkin','male','C++','1991-03-12'),
('Mila','Kunits','male','C++','1991-03-12');

create table teachers (
id BIGSERIAL NOT NULL PRIMARY KEY,
first_name VARCHAR(50),
last_name VARCHAR(50),
specialization VARCHAR(50),
experience VARCHAR(50)
);

INSERT INTO teachers (first_name, last_name, specialization, experience) VALUES('Tony', 'Stark','Java','10 years'),
('Bruce', 'Wayne','Phyton','5 years'),
('Clark', 'Kent','C++','3 years');

Select * from students, teachers
Where students.specialization = teachers.specialization;

Select students.id, students.first_name, students.last_name, students.specialization,
teachers.id, teachers.first_name, teachers.last_name
From students
Join teachers on teachers.specialization = students.specialization;
