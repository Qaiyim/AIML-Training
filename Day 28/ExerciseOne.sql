create database ExerciseOne

use ExerciseOne

create table StudentMarks (
    StudentID int primary key,
    StudentName nvarchar(50),
    Math int,
    Science int,
    English int,
    History int
)

insert into StudentMarks values (1,'Ahmad',90,82,75,80)

insert into StudentMarks values (2,'Qaiyim',95,80,83,89)
insert into StudentMarks values (3,'Imtan',90,70,70,87)
insert into StudentMarks values (4,'Fatehah',78,90,70,88)
insert into StudentMarks values (5,'Iman',93,83,78,88)

select * from StudentMarks
insert into StudentMarks values (6,'Aini',90,92,95,89)
select * from StudentMarks