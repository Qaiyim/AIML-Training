--create object objectName 

create database OurDb
--create table <TableName>
--(ColumnName DataType <constratint>,
    -------------
--	)

use OurDb

create table Student
(SId int primary key,
 SName nvarchar(50) not null,
 SFee float not null)

 --------------------------------------
 select * from Student
 insert into Student values (1,'Ahmad',5000.50)
 insert into Student values 
 (2,'Qaiyim',4500.25),
 (3,'Intan',5000.58),
 (4,'Fatehah',6000.58),
 (5,'Zainab',4000.28)
 select * from Student