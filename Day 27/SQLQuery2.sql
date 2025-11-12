use OurDb
-- Constraint, not null
-- primary key: not null and unique

create table Employee
(Id int primary key,
Firstname nvarchar(50)not null,
Lastname nvarchar(50))

select * from Employee
insert into Employee values (1,'Qaiyim','Shahabudin')
insert into Employee values (2,'Intan','Samsudin')
insert into Employee (Id,Firstname) values (3,'Fatehah')
select * from Employee
insert into Employee(Id,Lastname) values (5,'Ahmad')
-- Cannot insert the value NULL into column 'Firstname', table 'OurDb.dbo.Employee'; column does not allow nulls. INSERT fails.
insert into Employee (Id,Firstname) values (2,'Iman')
-- Violation of PRIMARY KEY constraint 'PK__Employee__3214EC0734098EEA'. Cannot insert duplicate key in object 'dbo.Employee'. The duplicate key value is (2).

delete from Employee
select * from Employee

drop table Employee
select * from Employee
------------------------------------------------------------------------------
-- default
create table Employee
(Id int primary key,
Firstname nvarchar(50) not null,
Lastname nvarchar(50),
City nvarchar(50) default ('Sungai Petani'))

insert into Employee values (1,'Qaiyim','Shahabudin','Changlun')
insert into Employee values (2,'Intan','Samsudin','Port Klang')
select * from Employee
insert into Employee (Id,Firstname,Lastname) values (3,'Iman','Soffea')
select * from Employee

-- Check
drop table Employee
create table Employee
(Id int primary key,
Firstname nvarchar(50) not null,
Lastname nvarchar(50),
City nvarchar(50) default ('Kuala Lumpur'),
Salary float not null check (Salary>=10000 and Salary<=50000))

insert into Employee (Id,Firstname,Lastname,Salary) values (1,'Qaiyim','Shahabudin',12000)
insert into Employee values (2,'Intan','Samsudin','Port Klang',9000)
-- The INSERT statement conflicted with the CHECK constraint "CK__Employee__Salary__5441852A". The conflict occurred in database "OurDb", table "dbo.Employee", column 'Salary'

insert into Employee values (2,'Rina','Harun','Merbok',15000)
select * from Employee

drop table Employee

create table Employee
(Id int primary key,
Firstname nvarchar(50) not null,
Mobile nvarchar(15) check (Mobile like '[0-9],[0-9],[0-9],[0-9],[0-9],[0-9],[0-9],[0-9],[0-9],[0-9]'))

insert into Employee values (1,'Qaiyim','0174131410')
select * from Employee

drop table Employee

create table Employee
(Id int primary key,
Firstname nvarchar(50) not null,
Mobile nvarchar(10) check (Mobile like '[0-9],[0-9],[0-9],[0-9],[0-9],[0-9],[0-9],[0-9],[0-9],[0-9]'))

select * from Employee

insert into Employee values (1,'Qaiyim','9876543210')
select * from Employee

insert into Employee values (3,'Riya','88999')
--The INSERT statement conflicted with the CHECK constraint "CK__Emp__Mobile__5441852A". The conflict occurred in database "OurDb", table "dbo.Emp", column 'Mobile'.
insert into Employee (Id,Firstname) values (3,'Riya')
insert into Employee values (4,'Rohan','9876543210')

--unique : not duplicate , allows null but once
drop table Employee

create table Employee
(Id int primary key,
Firstname nvarchar(50) not null, 
Mobile nvarchar(10) unique not null
check (Mobile like'[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]'),
Email nvarchar(100) unique
)
insert into Employee values (1,'Sam','9876543210','sam@yahoo.com')
insert into Employee values (2,'Ravi','9876543210','rav1256@yahoo.com')
-- Violation of UNIQUE KEY constraint 'UQ__Employee__6FAE0782B0658B06'. 
-- Cannot insert duplicate key in object 'dbo.Employee'. The duplicate key value is (9876543210).

insert into Employee (Id,Firstname,Mobile) values (3,'Qaiyim','9876543214')
insert into Employee (Id,Firstname,Mobile) values (4,'Intan','9845678128')
select*from Employee

-----------------------------------------------------------------------------------------
-- Identity (seed,increment)
drop table Student

create table Students
(SId int identity,
SName nvarchar(50) not null,
SFee float)

insert into Students(SName,SFee) values ('Ahmad',5000.50)
insert into Students(SName,SFee) values ('Qaiyim',3000.50)
insert into Students(SName,SFee) values ('Intan',4500.20)
select * from Students
insert into Students(SName,SFee) values ('Riya',4500.20)
----------------------------------------------------------
drop table Students
----------------------------------------------------------
create table Students
(SId int identity(100,5),
 SName nvarchar(50) not null,
 SFee float)
insert into Students(SName,SFee) values ('Ravi',5000.50)
insert into Students(SName,SFee) values ('Ani',3000.50)
insert into Students(SName,SFee) values ('Joy',4500.20)
select*from Students

  insert into Students(SName,SFee) values ('Riya',4500.20)
select* from Students
----------------------------------------------------------
create table Salary
(Grade varchar(1) primary key,
BasicSalary float,
HRA as BasicSalary*0.10  persisted,
TA as BasicSalary*0.15  persisted,
DA as BasicSalary *0.20  persisted)

insert into Salary values ('A',10000)
select * from Salary
insert into Salary values ('B',5000)

select Grade,BasicSalary,HRA,TA,DA, BasicSalary+TA+DA+HRA as 'Net Salary' from Salary 
insert into Salary values ('C',2000)
insert into Salary values ('D',1000)
select* from Salary

select max(BasicSalary) as 'Max Basic' from Salary
select min(BasicSalary) as 'Min Basic' from Salary
select avg(BasicSalary) as 'Avg Basic' from Salary
-----------------------------------------------------------------------------------------
-- Foreign Key
-------------------------------------------------------------------------------------------
create table Category
(CatId int primary key,
CategoryName nvarchar(50) not null unique
)

insert into Category values (1,'Electronics'),(2,'Clothing'),(3,'Home Decoration'),(4,'Mobile')
select * from Category order by CatId

create table Product
(PId int primary key identity,
PName nvarchar(50) not null ,
PPrice float not null ,
ProductCategory int foreign key references Category
)
insert into Product values ('IPhone-17',5000,4)
insert into Product values ('Nothing-3 a',2000,4)
insert into Product values ('Washing Machine',4000,1)

insert into Product values ('Shirt',200,2)
insert into Product values ('T-Shirt',199,2)
insert into Product values ('Jeans',399,2)
select * from Product

insert into Product values ('Reomote',209,5)
-- The INSERT statement conflicted with the FOREIGN KEY constraint "FK__Product__Product__693CA210". 
--    The conflict occurred in database "OurDb", table "dbo.Category", column 'CatId'.
select * from Category
select * from Product

-- Select column from table1 join table2 on Table1.CommonColumn=Table2.CommonColumn

select * from Product join Category 
on Product.ProductCategory=Category.CatId

select * from Product p join Category c
on p.ProductCategory=c.CatId

select  p.PId,p.PName,p.PPrice,p.ProductCategory,c.CategoryName 
from Product p join Category c
on p.ProductCategory=c.CatId

select  p.PId 'Product Id',p.PName 'Product Name',p.PPrice 'Product Price',
p.ProductCategory ,c.CategoryName  
from Product p join Category c
on p.ProductCategory=c.CatId

