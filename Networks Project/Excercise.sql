create table Projects(
projectNo int primary key,
projectTitle text,
employeeID int,
constraint FK1 foreign key(employeeID) references Employee(employeeID)
);

create table Employee(
employeeID int primary key,
emplyeeName text,
position text
);
Drop table Projects;
Alter table Employee drop position; 

insert into Employee values(1, "salah ali");
insert into Employee values(2, "samer kamel");
insert into Employee values(3, "hala taha");

insert into Projects values(1, "A", 1);
insert into Projects values(2, "B", 3);
insert into Projects values(3, "C", 2);
insert into Projects values(4, "D", 1);
insert into Projects values(5, "E", 2);

Delete from Projects where projectNo = 5;

select count(projectNo) from Projects where employeeID = 1; 

select emplyeeName from Employee, Projects where projectNo = 2 and Employee.employeeID = Projects.employeeID; 

select*from Projects;

create table Passwords(
username varchar(100) primary key,
password1 varchar(100)
);

select * from Users_Password;
Delete from Users_Password where user_name = "gabry";
