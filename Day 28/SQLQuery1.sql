create database SalesDb

use SalesDb
create table Products
(ProductID int primary key,
ProductName nvarchar (100),
Category nvarchar (50),
UnitPrice decimal(10,2))

delete from Products

insert into Products values (1,'Laptop Xiaomi','Electronics',1200)
select *from Products

insert into Products values 
(2,'Wireless Keyboard','Electronics',500),
(3,'Wireless Mouse','Electronics',650),
(4,'Earphone','Electronics',450),
(5,'Speaker','Electronics',2500),
(6,'Table','Furniture',4500),
(7,'Notebook','Stationary',25)

select * from Products

create table Sales
(SalesID int primary key identity,
ProductID int foreign key references Products(ProductID),
Region nvarchar(50) check (Region in ('East','West','North','South')),
Quantity int,
SalesDate date)

--YYYY-MM--DD
insert into Sales(ProductID,Region,Quantity,SalesDate) values (1,'East',5,'2024-02-23')
select * from Sales
insert into Sales
(ProductID,Region,Quantity,SalesDate)
values (2,'West',9,'2024-03-25'),
(3,'North',2,'2024-05-20'),
(4,'South',12,'2024-05-23'),
(5,'East',9,'2024-06-29'),
(6,'West',6,'2024-01-26')

select * from Sales
select * from Products

INSERT INTO Sales (ProductID, Region, Quantity, SaleSDate) VALUES
(1, 'East', 5, '2024-01-10'),
(2, 'West', 10, '2024-01-12'),
(3, 'North', 3, '2024-02-05'),
(4, 'South', 8, '2024-02-10'),
(5, 'East', 2, '2024-03-01'),
(1, 'West', 7, '2024-03-15'),
(3, 'North', 4, '2024-04-03'),
(2, 'South', 6, '2024-04-10'),
(5, 'East', 3, '2024-05-02'),
(4, 'West', 9, '2024-05-10')

select*from Sales