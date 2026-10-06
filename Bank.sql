create database banking_db;
use banking_db;
create table accounts (
     account_id INT primary key,
     customer_name varchar(100),
     account_type varchar(30),
     balance decimal(10,2),
     city varchar(50)
 );    
 insert into accounts values
 (101, 'arun', 'saving', 45000, 'hyderabad'),
 (102, 'meera', 'current', 85000, 'mubai'),
 (103, 'ravi', 'saving', 32000, 'hyderabad'),
 (104, 'priya', 'saving', 67000, 'bangalore');
 select * from accounts;
 DELIMITER //
 create procedure getallaccounts() 
 begin 
     select* from accounts;
 end //
DELIMITER //
 create procedure getaccountsbycity(in p_city varchar(50))
 begin 
     select* from accounts
     where city = p_city;
 end //
 DELIMITER ; 
 -- usage:
 call getaccountsbycity('hyderabad');
DELIMITER //
 create procedure getaccountsabovebalance(in p_balance decimal(10,2))
 begin 
     select* from accounts
     where balance > p_balance;
 end //
 DELIMITER ; 
 -- usage:
 call getaccountsabovebalance(50000);
DELIMITER //
create  procedure 