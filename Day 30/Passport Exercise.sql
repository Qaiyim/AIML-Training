create database PassportDb

use PassportDb
create table Person
(PersonID int primary key,
FullName nvarchar(50) not null,
DateofBirth date not null,
Nationality nvarchar(50) not null)

create table Passport
(PassportID nvarchar(50) primary key,
PersonID int not null unique foreign key references Person,
PassportNumber nvarchar(50) not null unique,
IssueDate date not null,
ExpiryDate date not null)

insert into Person values (101,'Ahmad Qaiyim bin Shahabudin','1999-01-05','Malaysia')
insert into Person values 
(102,'Intan Fatehah binti Samsudin','2000-09-01','Turkey'),
(103,'Aini Najihah binti Ridzuan','2000-01-08','Japan'),
(104,'Farah Najihah binti Roslan','1999-06-12','Malaysia'),
(105,'Farhan bin Azid','1999-02-05','Malaysia'),
(106,'Sofea Iman bin AKmal','1999-06-15','Japan')

select * from Person

insert into Passport values ('PP1001',101,'MY-9876','2024-01-15','2029-01-15')
insert into Passport values 
('PP1002',102,'TK-9873','2024-02-10','2029-02-10'),
('PP1003',103,'JP-9871','2024-03-20','2029-03-20'),
('PP1004',104,'MY-9823','2025-11-17','2030-11-17'),
('PP1005',105,'MY-9875','2025-02-10','2030-02-10'),
('PP1006',106,'JP-9823','2023-01-15','2027-01-15')

select * from Passport

select pr.PersonID,pr.FullName,pr.DateofBirth,pr.Nationality,
pp.PassportNumber,pp.ExpiryDate,pp.IssueDate from Passport pp join Person pr  
on pp.PersonID=pr.PersonID